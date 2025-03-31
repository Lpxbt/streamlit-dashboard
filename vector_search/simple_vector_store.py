#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Simple vector store implementation for the Business Trucks dashboard.
This module provides a simple vector store implementation using Redis.
"""

import os
import json
import logging
import numpy as np
from datetime import datetime

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('simple_vector_store')

class SimpleVectorStore:
    """Simple vector store implementation using Redis."""

    def __init__(self, redis_client=None, prefix="btagent:"):
        """Initialize the vector store."""
        self.redis_client = redis_client
        self.prefix = prefix
        logger.info("Initialized SimpleVectorStore")

    def add_vector(self, id, vector, metadata=None):
        """Add a vector to the store."""
        if not self.redis_client:
            logger.warning("Redis client not available, skipping add_vector")
            return False

        try:
            # Create key
            key = f"{self.prefix}vector:{id}"

            # Convert vector to JSON
            vector_json = json.dumps(vector.tolist() if hasattr(vector, 'tolist') else vector)

            # Create metadata
            if metadata is None:
                metadata = {}

            metadata_json = json.dumps(metadata)

            # Store in Redis
            self.redis_client.hset(key, "vector", vector_json)
            self.redis_client.hset(key, "metadata", metadata_json)
            self.redis_client.hset(key, "created_at", datetime.now().isoformat())

            logger.info(f"Added vector {id} to store")
            return True
        except Exception as e:
            logger.error(f"Error adding vector {id} to store: {e}")
            return False

    def get_vector(self, id):
        """Get a vector from the store."""
        if not self.redis_client:
            logger.warning("Redis client not available, skipping get_vector")
            return None

        try:
            # Create key
            key = f"{self.prefix}vector:{id}"

            # Get from Redis
            vector_json = self.redis_client.hget(key, "vector")
            metadata_json = self.redis_client.hget(key, "metadata")

            if not vector_json:
                logger.warning(f"Vector {id} not found in store")
                return None

            # Parse JSON
            vector = json.loads(vector_json)
            metadata = json.loads(metadata_json) if metadata_json else {}

            logger.info(f"Retrieved vector {id} from store")
            return {
                "id": id,
                "vector": vector,
                "metadata": metadata
            }
        except Exception as e:
            logger.error(f"Error getting vector {id} from store: {e}")
            return None

    def delete_vector(self, id):
        """Delete a vector from the store."""
        if not self.redis_client:
            logger.warning("Redis client not available, skipping delete_vector")
            return False

        try:
            # Create key
            key = f"{self.prefix}vector:{id}"

            # Delete from Redis
            self.redis_client.delete(key)

            logger.info(f"Deleted vector {id} from store")
            return True
        except Exception as e:
            logger.error(f"Error deleting vector {id} from store: {e}")
            return False

    def search(self, query_vector, k=5, threshold=0.0):
        """Search for similar vectors."""
        if not self.redis_client:
            logger.warning("Redis client not available, skipping search")
            return []

        try:
            # Get all vector keys
            all_keys = self.redis_client.keys(f"{self.prefix}vector:*")

            if not all_keys:
                logger.warning("No vectors found in store")
                return []

            # Convert query vector to numpy array
            query_vec = np.array(query_vector)
            query_vec = query_vec / np.linalg.norm(query_vec)

            # Calculate similarity for each vector
            results = []

            for key in all_keys:
                # Get vector
                vector_json = self.redis_client.hget(key, "vector")
                metadata_json = self.redis_client.hget(key, "metadata")

                if not vector_json:
                    continue

                # Parse JSON
                vector = json.loads(vector_json)
                metadata = json.loads(metadata_json) if metadata_json else {}

                # Calculate similarity
                vec = np.array(vector)
                vec = vec / np.linalg.norm(vec)
                similarity = np.dot(query_vec, vec)

                # Add to results if above threshold
                if similarity >= threshold:
                    # Extract ID from key
                    id = key.decode("utf-8").split(":")[-1] if isinstance(key, bytes) else key.split(":")[-1]

                    results.append({
                        "id": id,
                        "similarity": float(similarity),
                        "metadata": metadata
                    })

            # Sort by similarity (descending)
            results.sort(key=lambda x: x["similarity"], reverse=True)

            # Limit to top k
            results = results[:k]

            logger.info(f"Found {len(results)} similar vectors")
            return results
        except Exception as e:
            logger.error(f"Error searching for similar vectors: {e}")
            return []

    def get_all_vectors(self, limit=1000):
        """Get all vectors from the store."""
        if not self.redis_client:
            logger.warning("Redis client not available, skipping get_all_vectors")
            return []

        try:
            # Get all vector keys
            all_keys = self.redis_client.keys(f"{self.prefix}vector:*")

            if not all_keys:
                logger.warning("No vectors found in store")
                return []

            # Limit to avoid performance issues
            all_keys = all_keys[:limit]

            # Get all vectors
            vectors = []

            for key in all_keys:
                # Get vector
                vector_json = self.redis_client.hget(key, "vector")
                metadata_json = self.redis_client.hget(key, "metadata")

                if not vector_json:
                    continue

                # Parse JSON
                vector = json.loads(vector_json)
                metadata = json.loads(metadata_json) if metadata_json else {}

                # Extract ID from key
                id = key.decode("utf-8").split(":")[-1] if isinstance(key, bytes) else key.split(":")[-1]

                vectors.append({
                    "id": id,
                    "vector": vector,
                    "metadata": metadata
                })

            logger.info(f"Retrieved {len(vectors)} vectors from store")
            return vectors
        except Exception as e:
            logger.error(f"Error getting all vectors from store: {e}")
            return []

    def count_vectors(self):
        """Count the number of vectors in the store."""
        if not self.redis_client:
            logger.warning("Redis client not available, skipping count_vectors")
            return 0

        try:
            # Get all vector keys
            all_keys = self.redis_client.keys(f"{self.prefix}vector:*")
            count = len(all_keys)

            logger.info(f"Counted {count} vectors in store")
            return count
        except Exception as e:
            logger.error(f"Error counting vectors in store: {e}")
            return 0

    def clear(self):
        """Clear all vectors from the store."""
        if not self.redis_client:
            logger.warning("Redis client not available, skipping clear")
            return False

        try:
            # Get all vector keys
            all_keys = self.redis_client.keys(f"{self.prefix}vector:*")

            if not all_keys:
                logger.warning("No vectors found in store")
                return True

            # Delete all keys
            for key in all_keys:
                self.redis_client.delete(key)

            logger.info(f"Cleared {len(all_keys)} vectors from store")
            return True
        except Exception as e:
            logger.error(f"Error clearing vectors from store: {e}")
            return False
