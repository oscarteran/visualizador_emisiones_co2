
# Contribution Guide

## Table of Contents
- [How Can I Contribute?](#how-can-i-contribute)
- [Pull Requests](#pull-requests)
- [Code Style](#code-style)
- [Bug Reporting](#bug-reporting)

## How Can I Contribute?

1. Fork the repository
2. Create a branch for your contribution:
```bash
git checkout -b feature/YourFeatureName
```
Make your changes and document them
Ensure tests pass (if applicable)
Commit your changes:

```bash
git commit -m "feat: Concise description of the change"
```

Push your changes to your fork:

```bash
git push origin feature/YourFeatureName
```

Open a Pull Request

## Pull Requests
Guide to creating a Pull Request

Ensure your PR includes:

- A clear description of the objective
- References to related issues
- Screenshots (if applicable)

The description should follow this template:

```markdown
## Description
[Detailed description of the changes]

## Type of Change
- [ ] Bugfix
- [ ] Feature
- [ ] Code Improvement
- [ ] Documentation

## How Has This Been Tested?
[Description of the tests performed]

## Checklist
- [ ] My code follows the project style guidelines
- [ ] I have commented my code where necessary
- [ ] I have updated the documentation
- [ ] Tests pass locally
```

## Code Style

- Follow existing style conventions
- Use descriptive names for variables and functions
- Comment the code when necessary
- Follow Python’s style guide (PEP 8)

Commit Conventions
We use Conventional Commits:

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Formatting changes
- `refactor`: Code refactoring
- `test`: Add or modify tests
- `chore`: Maintenance tasks

Example:
```bash
feat: Add user input validation
```

## Bug Reporting
Before Reporting

- Check existing issues
- Verify you are using the latest version

### How to Report
Open an issue including:

- Clear description of the problem
- Steps to reproduce
- Expected behavior
- Current behavior
- Screenshots (if applicable)
- Environment (OS, Python version, etc.)

Bug Reporting Template
```markdown
## Bug Description
[Clear and concise description]

## Steps to Reproduce
1. Go to '...'
2. Click on '....'
3. Scroll to '....'
4. See error

## Expected Behavior
[Description]

## Current Behavior
[Description]

## Screenshots
[If applicable]

## Environment
 - OS: [e.g., Windows 10]
 - Python Version: [e.g., 3.8.0]
 - Relevant dependency versions
```
Additional Notes

- Ensure tests are up to date
- Keep changes focused and small
- Document significant changes
- Follow best security practices