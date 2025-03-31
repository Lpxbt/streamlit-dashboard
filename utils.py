#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Utility functions for the Business Trucks dashboard.
This module provides utility functions for the dashboard.
"""

import os
import json
import logging
import numpy as np
from datetime import datetime
import streamlit as st

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('utils')

class EmbeddingProvider:
    """Embedding provider for the dashboard."""

    def __init__(self):
        """Initialize the embedding provider."""
        self.model_name = st.secrets.get("embeddings", {}).get("model", "text-embedding-3-large")
        self.dimension = st.secrets.get("embeddings", {}).get("dimension", 1536)
        self.api_key = st.secrets.get("openrouter", {}).get("api_key", os.getenv("OPENROUTER_API_KEY"))
        logger.info(f"Initialized EmbeddingProvider with model {self.model_name}")

    def embed(self, texts):
        """Embed texts."""
        try:
            # For demo purposes, we'll just return random embeddings
            embeddings = []
            for _ in texts:
                embedding = np.random.randn(self.dimension)
                embedding = embedding / np.linalg.norm(embedding)
                embeddings.append(embedding.tolist())
            
            logger.info(f"Generated {len(embeddings)} embeddings")
            return embeddings
        except Exception as e:
            logger.error(f"Error generating embeddings: {e}")
            # Return random embeddings as fallback
            return [np.random.randn(self.dimension).tolist() for _ in texts]

class LLMProvider:
    """LLM provider for the dashboard."""

    def __init__(self):
        """Initialize the LLM provider."""
        self.model_name = st.secrets.get("openrouter", {}).get("model", "google/gemini-2.5-pro-exp-03-25:free")
        self.api_key = st.secrets.get("openrouter", {}).get("api_key", os.getenv("OPENROUTER_API_KEY"))
        logger.info(f"Initialized LLMProvider with model {self.model_name}")

    def generate(self, prompt):
        """Generate text."""
        try:
            # For demo purposes, we'll just return a mock response
            responses = {
                "Привет": "Здравствуйте! Я Анна, виртуальный ассистент компании Business Trucks. Чем я могу вам помочь?",
                "Какие грузовики вы продаете?": "Мы продаем различные модели коммерческого транспорта, включая КАМАЗ, МАЗ, ГАЗ, Hyundai и Isuzu. Какая марка вас интересует?",
                "Расскажите о КАМАЗ": "КАМАЗ предлагает различные модели грузовиков, включая КАМАЗ-5490 (седельный тягач), КАМАЗ-65115 (самосвал), КАМАЗ-43118 (бортовой грузовик повышенной проходимости), КАМАЗ-65207 (бортовой грузовик) и КАМАЗ-6520 (самосвал). Какая модель вас интересует?",
                "Какие условия финансирования?": "Мы предлагаем различные варианты финансирования: лизинг (от 10% первоначального взноса, срок до 60 месяцев), кредит (от 15% первоначального взноса, срок до 60 месяцев), программа Trade-in (обмен старой техники на новую с доплатой) и аренда с правом выкупа. Какой вариант вас интересует?"
            }
            
            # Check if prompt contains any of the keys
            for key, response in responses.items():
                if key.lower() in prompt.lower():
                    logger.info(f"Generated response for prompt containing '{key}'")
                    return response
            
            # Default response
            logger.info("Generated default response")
            return "Я Анна, виртуальный ассистент компании Business Trucks. Я могу рассказать вам о различных моделях коммерческого транспорта, условиях финансирования и ответить на другие вопросы о нашей компании. Чем я могу вам помочь?"
        except Exception as e:
            logger.error(f"Error generating text: {e}")
            return "Извините, у меня возникла проблема с генерацией ответа. Пожалуйста, попробуйте еще раз или свяжитесь с нашим менеджером."
