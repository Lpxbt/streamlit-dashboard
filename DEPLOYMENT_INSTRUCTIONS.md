# Deploying the Business Trucks Dashboard

This document provides instructions for deploying the Business Trucks Dashboard to GitHub and Streamlit Cloud.

## 1. Pushing to GitHub

1. Create a new repository on GitHub named 'streamlit-dashboard'
2. Use the provided script to push to GitHub:
   ```bash
   ./push_to_github.sh https://github.com/Lpxbt/streamlit-dashboard.git
   ```
   Replace the URL with your actual GitHub repository URL.

## 2. Deploying to Streamlit Cloud

1. Go to [Streamlit Cloud](https://share.streamlit.io/) and sign in with your GitHub account
2. Click on 'New app'
3. Select the repository, branch (main), and file (dashboard.py)
4. Click 'Deploy'
5. Once deployed, you can access your dashboard at https://username-repository-name.streamlit.app/

## 3. Setting Up Secrets

After deploying, you need to set up secrets in Streamlit Cloud:

1. Go to your app settings in Streamlit Cloud
2. Click on 'Secrets'
3. Add the following secrets:
   ```toml
   [redis]
   url = "redis://username:password@host:port"
   prefix = "btagent:"

   [openrouter]
   api_key = "your-openrouter-api-key"
   model = "google/gemini-2.5-pro-exp-03-25:free"

   [embeddings]
   model = "text-embedding-3-large"
   dimension = 1536

   [vector_search]
   similarity_threshold = 0.75
   max_results = 10

   [dashboard]
   enable_agent_chat = true
   enable_scraper_control = true
   enable_data_overview = true
   debug_mode = false
   ```

## 4. Verifying Deployment

1. After deployment, visit your app URL
2. Check that all tabs are working correctly
3. Test the vehicle search functionality
4. Test the agent chat if enabled
5. Verify that the documentation is displayed correctly

## 5. Troubleshooting

If you encounter issues:

1. Check the logs in Streamlit Cloud
2. Verify that all secrets are set correctly
3. Make sure Redis is accessible from Streamlit Cloud
4. Check that the OpenRouter API key is valid
5. Ensure all dependencies are installed correctly

## 6. Updating the Dashboard

To update the dashboard:

1. Make changes to the code locally
2. Commit the changes:
   ```bash
   git add .
   git commit -m "Description of changes"
   ```
3. Push to GitHub:
   ```bash
   git push
   ```
4. Streamlit Cloud will automatically redeploy the app
