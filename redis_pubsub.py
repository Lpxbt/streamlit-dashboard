#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Redis PubSub module for the Business Trucks dashboard.
This module provides functions for Redis PubSub.
"""

import os
import json
import logging
import threading
from datetime import datetime
import streamlit as st

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('redis_pubsub')

def get_redis_pubsub(redis_client=None):
    """Get a Redis PubSub instance."""
    if not redis_client:
        logger.warning("Redis client not available, returning mock PubSub")
        return MockRedisPubSub()
    
    try:
        # Create PubSub
        pubsub = redis_client.pubsub()
        logger.info("Created Redis PubSub")
        return RedisPubSub(redis_client, pubsub)
    except Exception as e:
        logger.error(f"Error creating Redis PubSub: {e}")
        return MockRedisPubSub()

class RedisPubSub:
    """Redis PubSub implementation."""

    def __init__(self, redis_client, pubsub):
        """Initialize the PubSub."""
        self.redis_client = redis_client
        self.pubsub = pubsub
        self.listeners = {}
        self.running = False
        self.thread = None
        logger.info("Initialized RedisPubSub")

    def subscribe(self, channel, callback):
        """Subscribe to a channel."""
        try:
            # Subscribe to channel
            self.pubsub.subscribe(channel)
            
            # Add callback to listeners
            self.listeners[channel] = callback
            
            # Start listening thread if not already running
            if not self.running:
                self.running = True
                self.thread = threading.Thread(target=self._listen)
                self.thread.daemon = True
                self.thread.start()
            
            logger.info(f"Subscribed to channel {channel}")
            return True
        except Exception as e:
            logger.error(f"Error subscribing to channel {channel}: {e}")
            return False

    def unsubscribe(self, channel):
        """Unsubscribe from a channel."""
        try:
            # Unsubscribe from channel
            self.pubsub.unsubscribe(channel)
            
            # Remove callback from listeners
            if channel in self.listeners:
                del self.listeners[channel]
            
            # Stop listening thread if no more listeners
            if not self.listeners and self.running:
                self.running = False
                if self.thread:
                    self.thread.join(timeout=1)
                    self.thread = None
            
            logger.info(f"Unsubscribed from channel {channel}")
            return True
        except Exception as e:
            logger.error(f"Error unsubscribing from channel {channel}: {e}")
            return False

    def publish(self, channel, message):
        """Publish a message to a channel."""
        try:
            # Convert message to JSON if it's a dict
            if isinstance(message, dict):
                message = json.dumps(message)
            
            # Publish message
            self.redis_client.publish(channel, message)
            
            logger.info(f"Published message to channel {channel}")
            return True
        except Exception as e:
            logger.error(f"Error publishing message to channel {channel}: {e}")
            return False

    def _listen(self):
        """Listen for messages."""
        try:
            for message in self.pubsub.listen():
                if not self.running:
                    break
                
                if message["type"] == "message":
                    channel = message["channel"]
                    data = message["data"]
                    
                    # Convert channel to string if it's bytes
                    if isinstance(channel, bytes):
                        channel = channel.decode("utf-8")
                    
                    # Convert data to string if it's bytes
                    if isinstance(data, bytes):
                        data = data.decode("utf-8")
                    
                    # Try to parse data as JSON
                    try:
                        data = json.loads(data)
                    except:
                        pass
                    
                    # Call callback if exists
                    if channel in self.listeners:
                        try:
                            self.listeners[channel](data)
                        except Exception as e:
                            logger.error(f"Error calling callback for channel {channel}: {e}")
        except Exception as e:
            logger.error(f"Error listening for messages: {e}")
            self.running = False

class MockRedisPubSub:
    """Mock Redis PubSub implementation."""

    def __init__(self):
        """Initialize the mock PubSub."""
        self.listeners = {}
        logger.info("Initialized MockRedisPubSub")

    def subscribe(self, channel, callback):
        """Subscribe to a channel."""
        try:
            # Add callback to listeners
            self.listeners[channel] = callback
            
            logger.info(f"Subscribed to channel {channel} (mock)")
            return True
        except Exception as e:
            logger.error(f"Error subscribing to channel {channel} (mock): {e}")
            return False

    def unsubscribe(self, channel):
        """Unsubscribe from a channel."""
        try:
            # Remove callback from listeners
            if channel in self.listeners:
                del self.listeners[channel]
            
            logger.info(f"Unsubscribed from channel {channel} (mock)")
            return True
        except Exception as e:
            logger.error(f"Error unsubscribing from channel {channel} (mock): {e}")
            return False

    def publish(self, channel, message):
        """Publish a message to a channel."""
        try:
            # Convert message to JSON if it's a dict
            if isinstance(message, dict):
                message = json.dumps(message)
            
            logger.info(f"Published message to channel {channel} (mock)")
            
            # Call callback if exists
            if channel in self.listeners:
                try:
                    self.listeners[channel](message)
                except Exception as e:
                    logger.error(f"Error calling callback for channel {channel} (mock): {e}")
            
            return True
        except Exception as e:
            logger.error(f"Error publishing message to channel {channel} (mock): {e}")
            return False
