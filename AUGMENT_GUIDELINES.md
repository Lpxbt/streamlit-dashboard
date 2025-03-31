# Augment AI Guidelines

These guidelines help ensure that the AI assistant provides high-quality, consistent, and effective assistance for the Business Trucks project.

## Core Guidelines

1. **MCP Server Management**: Always verify MCP servers are running before starting tasks. If servers are not running, start them using the run_all_mcp_servers.sh script.

2. **Testing Protocol**: Thoroughly test all implementations before marking tasks as complete. Write unit tests when appropriate and verify functionality across different scenarios.

3. **Tool Selection**: Use MCP server tools when interacting with external systems, web content, or performing complex operations. Choose the most appropriate tool for each specific task.

4. **Documentation Standards**: Create comprehensive documentation including setup instructions, usage examples, and API references. Document both code and processes clearly.

5. **Project Structure**: Maintain the established project organization with BtAgent and AgentKnowledge as primary folders. Place new files in appropriate locations following existing patterns.

6. **Incremental Development**: Break complex tasks into smaller, manageable steps. Validate each step before proceeding to the next one.

7. **Error Handling**: Implement robust error handling with informative error messages. Consider edge cases and provide graceful fallbacks.

8. **Performance Optimization**: Monitor resource usage and optimize code for efficiency. Consider caching strategies and asynchronous processing when appropriate.

9. **Security Practices**: Follow security best practices when handling sensitive data. Never expose API keys or credentials in code or logs.

10. **User Experience**: Design interfaces and interactions with the end user in mind. Provide clear feedback and intuitive workflows.

11. **Task Completion Checklist**: Before marking a task complete, ensure all code is tested, documented, and follows project standards. Document all changes in README files and the testing webpage.

## Specific Guidelines for Business Trucks Project

### Redis AI Tools

1. **Vector Search**: Implement vector search using Redis as the backend. Use the SimpleVectorStore class for basic functionality.

2. **RAG System**: Implement a Retrieval-Augmented Generation system using Redis and LangChain. Use the SimpleRAG class for basic functionality.

3. **Session Management**: Use Redis for session management. Store conversation history and user preferences in Redis.

4. **Caching**: Use Redis for caching API responses and expensive computations. Implement TTL (Time-To-Live) for cache entries.

### AvitoScraping

1. **Rate Limiting**: Implement rate limiting to avoid being blocked by Avito.ru. Use random delays between requests.

2. **Proxy Rotation**: Use proxy rotation to avoid IP bans. Implement fallback mechanisms for failed proxies.

3. **Captcha Handling**: Implement captcha detection and solving. Use captcha solving services when necessary.

4. **Data Schema**: Follow the established data schema for vehicle data. Include all required fields and validate data before storing.

5. **Incremental Updates**: Implement incremental updates to avoid re-scraping all data. Use timestamps to track changes.

### LangChain Integration

1. **Custom Components**: Create custom LangChain components for the Business Trucks project. Implement CustomEmbeddings and CustomLLM classes.

2. **Chain Construction**: Use LangChain's chain construction to create complex workflows. Implement ConversationalRetrievalChain for chat functionality.

3. **Tool Integration**: Integrate LangChain with external tools using the Tool class. Implement tools for vehicle search, financing calculation, etc.

4. **Agent Configuration**: Configure LangChain agents with appropriate tools and memory. Use the AgentExecutor class for agent execution.

5. **Prompt Engineering**: Create effective prompts for LangChain components. Include system messages, user messages, and examples.

### Streamlit Dashboard

1. **Page Organization**: Organize the dashboard into logical pages. Use st.sidebar for navigation.

2. **Data Visualization**: Create informative visualizations for vehicle data. Use appropriate chart types for different data.

3. **User Interaction**: Implement intuitive user interactions. Use appropriate input widgets for different data types.

4. **Error Handling**: Implement error handling for user inputs and API calls. Display informative error messages.

5. **Performance**: Optimize dashboard performance. Use caching and session state to avoid redundant computations.

## Implementation Checklist

Before marking a task as complete, ensure that:

- [ ] All code is tested and working correctly
- [ ] Documentation is complete and accurate
- [ ] Error handling is implemented
- [ ] Performance is optimized
- [ ] Security best practices are followed
- [ ] User experience is considered
- [ ] Changes are documented in README files
- [ ] Changes are documented in the testing webpage
