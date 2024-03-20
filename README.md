# SA_A6_APIEvolution_Python
Software Architecture Assignment 6: Create and document the evolution of an API showing the initial version, a second version with deprecation, and a final version

# Configuring Doxygen:

Marking items as deprecated in doxygen:Python, must be done using the \deprecated special command. Special commands are enabled in python code using the '''! <content> ''' format within python docstrings.
To denote doxygen:Python class properties (attributes) as deprecated requires the: ## \deprecated <text> prefix to each attribute.

In generating the doxygen docs, the config file was generated using the "doxygen -g apidocs" command within each version directory.
Additionally, the doxygen config file was manually updated with the following tags for each version:
- "INPUT" = ./source (the "source" directory within each version.)
- "RECURSIVE" = YES