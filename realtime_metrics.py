#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Real-time metrics module for the Business Trucks dashboard.
This module provides functions for real-time metrics.
"""

import os
import json
import logging
from datetime import datetime
import streamlit as st

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('realtime_metrics')

def get_realtime_metrics(redis_client=None):
    """Get real-time metrics."""
    if not redis_client:
        logger.warning("Redis client not available, returning mock metrics")
        return MockRealtimeMetrics()
    
    try:
        # Create metrics
        metrics = RealtimeMetrics(redis_client)
        logger.info("Created real-time metrics")
        return metrics
    except Exception as e:
        logger.error(f"Error creating real-time metrics: {e}")
        return MockRealtimeMetrics()

class RealtimeMetrics:
    """Real-time metrics implementation."""

    def __init__(self, redis_client):
        """Initialize the metrics."""
        self.redis_client = redis_client
        self.prefix = "btagent:"
        logger.info("Initialized RealtimeMetrics")

    def get_metrics(self):
        """Get metrics."""
        try:
            # Get vehicle count
            vehicle_count = self.redis_client.scard(f"{self.prefix}vehicles")
            
            # Get vehicle count by category
            vehicle_count_by_category = {}
            categories = self.redis_client.smembers(f"{self.prefix}categories")
            for category in categories:
                category_str = category.decode("utf-8") if isinstance(category, bytes) else category
                count = self.redis_client.scard(f"{self.prefix}category:{category_str}")
                vehicle_count_by_category[category_str] = count
            
            # Get search count
            search_count = self.redis_client.get(f"{self.prefix}search_count")
            search_count = int(search_count) if search_count else 0
            
            # Get scraper status
            scraper_status = self.redis_client.get(f"{self.prefix}scraper_status")
            scraper_status = scraper_status.decode("utf-8") if isinstance(scraper_status, bytes) else "idle"
            
            # Get scraper progress
            scraper_progress = self.redis_client.get(f"{self.prefix}scraper_progress")
            scraper_progress = float(scraper_progress) if scraper_progress else 0.0
            
            # Get scraper last update
            scraper_last_update = self.redis_client.get(f"{self.prefix}scraper_last_update")
            scraper_last_update = datetime.fromisoformat(scraper_last_update.decode("utf-8")) if scraper_last_update else None
            
            logger.info("Retrieved metrics")
            return {
                "vehicle_count": vehicle_count,
                "vehicle_count_by_category": vehicle_count_by_category,
                "search_count": search_count,
                "scraper_status": scraper_status,
                "scraper_progress": scraper_progress,
                "scraper_last_update": scraper_last_update,
                "last_update": datetime.now()
            }
        except Exception as e:
            logger.error(f"Error getting metrics: {e}")
            return self._get_mock_metrics()

    def update_search_stats(self, query):
        """Update search stats."""
        try:
            # Increment search count
            self.redis_client.incr(f"{self.prefix}search_count")
            
            # Add search to history
            search_data = {
                "query": query,
                "timestamp": datetime.now().isoformat()
            }
            self.redis_client.lpush(f"{self.prefix}search_history", json.dumps(search_data))
            self.redis_client.ltrim(f"{self.prefix}search_history", 0, 99)  # Keep only the last 100 searches
            
            logger.info(f"Updated search stats for query: {query}")
            return True
        except Exception as e:
            logger.error(f"Error updating search stats: {e}")
            return False

    def update_scraper_status(self, status, progress=0.0):
        """Update scraper status."""
        try:
            # Set scraper status
            self.redis_client.set(f"{self.prefix}scraper_status", status)
            
            # Set scraper progress
            self.redis_client.set(f"{self.prefix}scraper_progress", progress)
            
            # Set scraper last update
            self.redis_client.set(f"{self.prefix}scraper_last_update", datetime.now().isoformat())
            
            logger.info(f"Updated scraper status: {status}, progress: {progress}")
            return True
        except Exception as e:
            logger.error(f"Error updating scraper status: {e}")
            return False

    def update_agent_stats(self):
        """Update agent stats."""
        try:
            # Increment conversation count
            self.redis_client.incr(f"{self.prefix}conversation_count")
            
            # Increment message count
            self.redis_client.incr(f"{self.prefix}message_count")
            
            logger.info("Updated agent stats")
            return True
        except Exception as e:
            logger.error(f"Error updating agent stats: {e}")
            return False

    def _get_mock_metrics(self):
        """Get mock metrics."""
        return {
            "vehicle_count": 120,
            "vehicle_count_by_category": {
                "trucks": 45,
                "vans": 35,
                "buses": 20,
                "tractors": 10,
                "construction": 5,
                "agricultural": 5,
                "trailers": 0
            },
            "search_count": 250,
            "scraper_status": "idle",
            "scraper_progress": 0.0,
            "scraper_last_update": datetime.now(),
            "last_update": datetime.now()
        }

class MockRealtimeMetrics:
    """Mock real-time metrics implementation."""

    def __init__(self):
        """Initialize the mock metrics."""
        logger.info("Initialized MockRealtimeMetrics")

    def get_metrics(self):
        """Get mock metrics."""
        return {
            "vehicle_count": 120,
            "vehicle_count_by_category": {
                "trucks": 45,
                "vans": 35,
                "buses": 20,
                "tractors": 10,
                "construction": 5,
                "agricultural": 5,
                "trailers": 0
            },
            "search_count": 250,
            "scraper_status": "idle",
            "scraper_progress": 0.0,
            "scraper_last_update": datetime.now(),
            "last_update": datetime.now()
        }

    def update_search_stats(self, query):
        """Update search stats (mock)."""
        logger.info(f"Updated search stats for query: {query} (mock)")
        return True

    def update_scraper_status(self, status, progress=0.0):
        """Update scraper status (mock)."""
        logger.info(f"Updated scraper status: {status}, progress: {progress} (mock)")
        return True

    def update_agent_stats(self):
        """Update agent stats (mock)."""
        logger.info("Updated agent stats (mock)")
        return True
