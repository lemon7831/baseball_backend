import os

# GCS 設定
GCS_BUCKET_NAME = "baseball_storage"

# 外部 API 端點
POSE_API_URL = "https://mmpose-api-new-924124779607.europe-west1.run.app/pose_video"
BALL_API_URL = "https://base-ball-detect-api-1069614647348.us-east4.run.app/predict"

# Render PostgreSQL 資料庫 URL
DATABASE_URL = os.environ.get("DATABASE_URL", "postgresql://baseball_user:OLBaWJBRAYnAu01pfOFNtNp5CZkjsH09@dpg-d2iao163jp1c7399edog-a.oregon-postgres.render.com/baseball_db_4kcp")
# LemonAPI
# POSE_API_URL = "http://localhost:8000/pose_video"
# BALL_API_URL = "http://localhost:8080/predict"
