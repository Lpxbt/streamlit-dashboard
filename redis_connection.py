#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Redis connection module for the Business Trucks dashboard.
This module provides functions for connecting to Redis and retrieving data.
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
logger = logging.getLogger('redis_connection')

def get_redis_client():
    """Get a Redis client instance."""
    try:
        # Try to get Redis URL from Streamlit secrets
        redis_url = st.secrets.get("redis", {}).get("url", None)
        
        # If not found in secrets, try environment variable
        if not redis_url:
            redis_url = os.getenv("REDIS_URL")
        
        # If still not found, use a default URL for local development
        if not redis_url:
            logger.warning("Redis URL not found in secrets or environment variables. Using default local URL.")
            redis_url = "redis://localhost:6379"
        
        # Get Redis prefix from secrets or environment
        redis_prefix = st.secrets.get("redis", {}).get("prefix", "btagent:")
        if not redis_prefix:
            redis_prefix = os.getenv("REDIS_PREFIX", "btagent:")
        
        # For the demo, we'll just return mock data
        logger.info("Using mock data instead of connecting to Redis")
        return None, redis_prefix
    except Exception as e:
        logger.error(f"Error connecting to Redis: {e}")
        return None, "btagent:"

def get_mock_data():
    """Get mock data for testing."""
    # Mock vehicle data
    vehicles = [
        {
            "id": "1",
            "make": "КАМАЗ",
            "model": "5490",
            "year": 2022,
            "price": 4800000,
            "city": "Москва",
            "seller_type": "Дилер",
            "url": "https://www.avito.ru/moskva/gruzoviki_i_spetstehnika/kamaz_5490_2022_2639401234",
            "description": "Седельный тягач КАМАЗ 5490 в отличном состоянии. Пробег 150 000 км. Один владелец. Полный комплект документов.",
            "image_url": "https://via.placeholder.com/300x200.png?text=КАМАЗ+5490",
            "created_at": "2025-03-15T12:00:00Z",
            "updated_at": "2025-04-01T12:00:00Z"
        },
        {
            "id": "2",
            "make": "МАЗ",
            "model": "6501",
            "year": 2021,
            "price": 5200000,
            "city": "Санкт-Петербург",
            "seller_type": "Дилер",
            "url": "https://www.avito.ru/sankt-peterburg/gruzoviki_i_spetstehnika/maz_6501_2021_2639401235",
            "description": "Самосвал МАЗ 6501 в отличном состоянии. Пробег 100 000 км. Один владелец. Полный комплект документов.",
            "image_url": "https://via.placeholder.com/300x200.png?text=МАЗ+6501",
            "created_at": "2025-03-16T12:00:00Z",
            "updated_at": "2025-04-01T12:00:00Z"
        },
        {
            "id": "3",
            "make": "ГАЗ",
            "model": "ГАЗель Next",
            "year": 2023,
            "price": 1800000,
            "city": "Екатеринбург",
            "seller_type": "Частное лицо",
            "url": "https://www.avito.ru/ekaterinburg/gruzoviki_i_spetstehnika/gazel_next_2023_2639401236",
            "description": "ГАЗель Next в отличном состоянии. Пробег 50 000 км. Один владелец. Полный комплект документов.",
            "image_url": "https://via.placeholder.com/300x200.png?text=ГАЗель+Next",
            "created_at": "2025-03-17T12:00:00Z",
            "updated_at": "2025-04-01T12:00:00Z"
        },
        {
            "id": "4",
            "make": "Hyundai",
            "model": "HD78",
            "year": 2022,
            "price": 3100000,
            "city": "Новосибирск",
            "seller_type": "Дилер",
            "url": "https://www.avito.ru/novosibirsk/gruzoviki_i_spetstehnika/hyundai_hd78_2022_2639401237",
            "description": "Hyundai HD78 в отличном состоянии. Пробег 80 000 км. Один владелец. Полный комплект документов.",
            "image_url": "https://via.placeholder.com/300x200.png?text=Hyundai+HD78",
            "created_at": "2025-03-18T12:00:00Z",
            "updated_at": "2025-04-01T12:00:00Z"
        },
        {
            "id": "5",
            "make": "Isuzu",
            "model": "NMR85",
            "year": 2023,
            "price": 3000000,
            "city": "Казань",
            "seller_type": "Дилер",
            "url": "https://www.avito.ru/kazan/gruzoviki_i_spetstehnika/isuzu_nmr85_2023_2639401238",
            "description": "Isuzu NMR85 в отличном состоянии. Пробег 60 000 км. Один владелец. Полный комплект документов.",
            "image_url": "https://via.placeholder.com/300x200.png?text=Isuzu+NMR85",
            "created_at": "2025-03-19T12:00:00Z",
            "updated_at": "2025-04-01T12:00:00Z"
        }
    ]
    
    # Mock agent stats
    agent_stats = {
        "total_conversations": 1250,
        "total_messages": 8750,
        "average_conversation_length": 7,
        "average_response_time": 1.2,
        "top_queries": [
            {"query": "КАМАЗ", "count": 350},
            {"query": "ГАЗель", "count": 280},
            {"query": "МАЗ", "count": 220},
            {"query": "Hyundai", "count": 180},
            {"query": "Isuzu", "count": 150}
        ],
        "daily_conversations": [
            {"date": "2025-03-25", "count": 42},
            {"date": "2025-03-26", "count": 38},
            {"date": "2025-03-27", "count": 45},
            {"date": "2025-03-28", "count": 50},
            {"date": "2025-03-29", "count": 35},
            {"date": "2025-03-30", "count": 30},
            {"date": "2025-03-31", "count": 40}
        ]
    }
    
    # Mock scraper stats
    scraper_stats = {
        "total_listings": 12500,
        "new_listings_today": 250,
        "updated_listings_today": 500,
        "average_price": 3500000,
        "top_makes": [
            {"make": "КАМАЗ", "count": 3500},
            {"make": "ГАЗ", "count": 2800},
            {"make": "МАЗ", "count": 2200},
            {"make": "Hyundai", "count": 1800},
            {"make": "Isuzu", "count": 1500}
        ],
        "daily_listings": [
            {"date": "2025-03-25", "count": 220},
            {"date": "2025-03-26", "count": 240},
            {"date": "2025-03-27", "count": 260},
            {"date": "2025-03-28", "count": 280},
            {"date": "2025-03-29", "count": 200},
            {"date": "2025-03-30", "count": 180},
            {"date": "2025-03-31", "count": 250}
        ]
    }
    
    # Mock system status
    system_status = {
        "status": "online",
        "last_update": datetime.now().isoformat(),
        "components": {
            "agent": "online",
            "scraper": "online",
            "database": "online",
            "redis": "online"
        },
        "uptime": "7 days, 12 hours, 34 minutes",
        "memory_usage": "1.2 GB",
        "cpu_usage": "25%"
    }
    
    # Mock recent searches
    recent_searches = [
        {"query": "КАМАЗ 5490", "timestamp": "2025-04-01T11:30:00Z", "results": 15},
        {"query": "ГАЗель Next", "timestamp": "2025-04-01T11:15:00Z", "results": 12},
        {"query": "МАЗ 6501", "timestamp": "2025-04-01T11:00:00Z", "results": 8},
        {"query": "Hyundai HD78", "timestamp": "2025-04-01T10:45:00Z", "results": 10},
        {"query": "Isuzu NMR85", "timestamp": "2025-04-01T10:30:00Z", "results": 7}
    ]
    
    # Mock recent conversations
    recent_conversations = [
        {
            "id": "1",
            "user": "user123",
            "timestamp": "2025-04-01T11:30:00Z",
            "messages": [
                {"role": "user", "content": "Привет! Я ищу грузовик КАМАЗ. Что вы можете предложить?"},
                {"role": "assistant", "content": "Здравствуйте! КАМАЗ предлагает различные модели грузовиков, включая КАМАЗ-5490 (седельный тягач), КАМАЗ-65115 (самосвал), КАМАЗ-43118 (бортовой грузовик повышенной проходимости), КАМАЗ-65207 (бортовой грузовик) и КАМАЗ-6520 (самосвал). Какая модель вас интересует?"}
            ]
        },
        {
            "id": "2",
            "user": "user456",
            "timestamp": "2025-04-01T11:15:00Z",
            "messages": [
                {"role": "user", "content": "Какие условия финансирования вы предлагаете?"},
                {"role": "assistant", "content": "Мы предлагаем различные варианты финансирования: лизинг (от 10% первоначального взноса, срок до 60 месяцев), кредит (от 15% первоначального взноса, срок до 60 месяцев), программа Trade-in (обмен старой техники на новую с доплатой) и аренда с правом выкупа. Какой вариант вас интересует?"}
            ]
        }
    ]
    
    return {
        "vehicles": vehicles,
        "agent_stats": agent_stats,
        "scraper_stats": scraper_stats,
        "system_status": system_status,
        "recent_searches": recent_searches,
        "recent_conversations": recent_conversations
    }

# Initialize mock data
mock_data = get_mock_data()

def get_data(client, prefix, data_type):
    """Get data from Redis or mock data if Redis is not available."""
    # Return mock data
    return mock_data.get(data_type, [])
