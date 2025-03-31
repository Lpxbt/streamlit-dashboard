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

## Implementation Best Practices

### Code Quality

- Write clean, readable, and maintainable code
- Follow PEP 8 style guidelines for Python code
- Use meaningful variable and function names
- Add comments to explain complex logic
- Implement proper error handling

### Documentation

- Document all functions, classes, and modules
- Include examples in documentation
- Update README files when adding new features
- Create user guides for complex functionality
- Document API endpoints and parameters

### Testing

- Write unit tests for all new functionality
- Test edge cases and error conditions
- Verify performance under load
- Test across different environments
- Document test procedures and results

### Security

- Never hardcode credentials in source code
- Use environment variables for sensitive information
- Implement proper authentication and authorization
- Validate all user inputs
- Follow the principle of least privilege

### Deployment

- Document deployment procedures
- Create backup and recovery plans
- Monitor system performance
- Implement logging for troubleshooting
- Create alerts for critical issues

## Project-Specific Guidelines

### AvitoScraping

- Implement rate limiting to avoid being blocked
- Rotate user agents and IP addresses
- Handle pagination properly
- Extract all required data fields
- Store data in the appropriate database tables
- Update data daily as specified

### Redis AI Tools

- Optimize vector search for performance
- Implement proper caching strategies
- Handle large datasets efficiently
- Ensure real-time updates work correctly
- Implement proper error handling for Redis operations

### Business Trucks Website

- Ensure all content is in Russian
- Follow the brand guidelines
- Optimize for mobile devices
- Implement proper SEO
- Ensure fast loading times
