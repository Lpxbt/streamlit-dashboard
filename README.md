# Business Trucks Dashboard

A comprehensive dashboard for the Business Trucks AI Sales Agent project, built with Streamlit.

## Features

- **Dashboard Overview**: Real-time metrics and system status
- **Vehicle Search**: Search for vehicles using natural language
- **Data Overview**: View and filter vehicle data
- **Scraper Control**: Control the AvitoScraping agent
- **Agent Chat**: Chat with the AI agent
- **Implementation Documentation**: Documentation with the following tabs:
  - **Project Overview**: Overview of the implementation and components
  - **Augment Guidelines**: Guidelines for AI assistants working on the project
  - **Technical Details**: Detailed technical information and code examples

## Live Demo

You can see a live demo of the dashboard at: https://scotty.streamlit.app/

## Setup

### Local Development

1. Clone this repository:
   ```bash
   git clone https://github.com/Lpxbt/streamlit-dashboard.git
   cd streamlit-dashboard
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file with your credentials:
   ```
   REDIS_URL=your_redis_url
   OPENROUTER_API_KEY=your_openrouter_api_key
   ```

4. Run the dashboard:
   ```bash
   streamlit run dashboard.py
   ```

### Deployment

The dashboard is automatically deployed to Streamlit Cloud when changes are pushed to the main branch.

## Project Structure

- `dashboard.py`: Main Streamlit application
- `simple_rag.py`: Simple RAG system implementation
- `langchain_integration.py`: LangChain integration
- `search_vehicles.py`: Search for vehicles in Redis
- `import_avito_data.py`: Import scraped data into Redis
- `check_data.py`: Check the data in Redis
- `AUGMENT_GUIDELINES.md`: Guidelines for AI assistants

## Technologies Used

- **Streamlit**: Dashboard framework
- **Redis**: Vector database for storing vehicle data
- **LangChain**: Enhanced RAG and agent capabilities
- **OpenRouter API**: LLM provider for text generation
- **Sentence Transformers**: Embedding model for vector search

## Related Projects

- [BtAgent](https://github.com/Lpxbt/augmentbot/tree/main/BtAgent): Business Trucks AI Sales Agent
- [AgentKnowledge](https://github.com/Lpxbt/augmentbot/tree/main/AgentKnowledge): Knowledge base for the AI agent
- [AvitoScraping](https://github.com/Lpxbt/augmentbot/tree/main/AvitoScraping): Data collection from Avito.ru
