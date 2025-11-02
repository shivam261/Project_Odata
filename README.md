# OData Backend API

A modern, asynchronous FastAPI backend application with PostgreSQL database, featuring a modular architecture and comprehensive testing suite.

## 🚀 Features

- **🏗️ Modular Architecture**: Clean separation of concerns with service pattern implementation
- **⚡ Async/Await**: Full asynchronous support for high-performance operations
- **🗄️ PostgreSQL Database**: Production-ready PostgreSQL with async SQLModel/SQLAlchemy
- **🔄 Database Migrations**: Alembic integration for seamless database schema management
- **🧪 Comprehensive Testing**: Async test suite with SQLite for isolated testing
- **📦 Modern Package Management**: UV for fast and reliable dependency management
- **🔐 Authentication System**: User registration and login endpoints
- **🏷️ Type Safety**: Full type hints with Pydantic models

## 📁 Project Structure

```
odata_backend/
├── src/                          # Source code
│   ├── auth/                     # Authentication module
│   │   ├── model.py             # User data models
│   │   ├── router.py            # Auth API endpoints
│   │   ├── service.py           # Business logic layer
│   │   ├── schemas.py           # Request/Response schemas
│   │   └── exceptions.py        # Custom exceptions
│   ├── dashboard/               # Dashboard module
│   ├── integration_content/     # Integration content module
│   ├── log_files/              # Log files module
│   ├── message_mapping/        # Message mapping module
│   ├── message_processsing_logs/ # Message processing logs
│   ├── security_content/       # Security content module
│   ├── middlewares/            # Custom middlewares
│   ├── config.py               # Configuration settings
│   ├── database.py             # Database connection and session management
│   ├── exception.py            # Global exception handlers
│   └── models.py               # Shared data models
├── alembic/                    # Database migrations
│   ├── versions/               # Migration files
│   └── env.py                  # Alembic configuration
├── tests/                      # Test suite
│   ├── conftest.py            # Pytest fixtures and configuration
│   └── test_auth.py           # Authentication tests
├── main.py                     # FastAPI application entry point
├── alembic.ini                # Alembic configuration
├── pyproject.toml             # Project dependencies and metadata
├── uv.lock                    # Dependency lock file
└── README.md                  # This file
```

## 🛠️ Technology Stack

### Core Framework
- **FastAPI**: Modern, fast web framework for building APIs
- **SQLModel**: SQL databases in Python, designed for FastAPI
- **SQLAlchemy**: Python SQL toolkit with async support
- **Pydantic**: Data validation and parsing using Python type hints

### Database
- **PostgreSQL**: Primary production database
- **SQLite**: Testing database for isolated test runs
- **Alembic**: Database migration tool
- **aiosqlite**: Async SQLite driver for testing

### Development Tools
- **UV**: Ultra-fast Python package installer and resolver
- **pytest**: Testing framework with async support
- **pytest-asyncio**: Async test support
- **HTTPX**: Async HTTP client for testing

### Service Pattern Architecture

The application follows a clean service pattern with clear separation of concerns:

- **Models**: Data models and database schemas (`model.py`)
- **Routers**: API endpoint definitions (`router.py`)
- **Services**: Business logic and data processing (`service.py`)
- **Schemas**: Request/Response data validation (`schemas.py`)
- **Exceptions**: Custom error handling (`exceptions.py`)

## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- PostgreSQL database
- UV package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd odata_backend
   ```

2. **Install UV** (if not already installed)
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

3. **Install dependencies with UV**
   ```bash
   uv sync
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your database credentials
   ```

   Required environment variables:
   ```env
   POSTGRES_SERVICE_URL=postgresql+asyncpg://user:password@localhost/dbname
   ```

5. **Run database migrations**
   ```bash
   uv run alembic upgrade head
   ```

6. **Start the development server**
   ```bash
   uv run fastapi dev main.py
   ```

The API will be available at `http://localhost:8000`

## 🧪 Testing

### Running Tests

The project includes a comprehensive async test suite using pytest with SQLite for database isolation.

```bash
# Run all tests
uv run pytest

# Run with verbose output
uv run pytest -v

# Run specific test file
uv run pytest tests/test_auth.py -v

# Run specific test
uv run pytest tests/test_auth.py::test_login_success -v
```

### Test Features

- **Async Testing**: All tests use `@pytest.mark.asyncio` for async support
- **Database Isolation**: Each test uses a temporary SQLite database
- **Automatic Cleanup**: Test databases are automatically deleted after tests
- **HTTPX Integration**: Async HTTP client for endpoint testing
- **Fixture-based Setup**: Reusable test fixtures for database and client setup

### Test Coverage

- ✅ User Registration (success, duplicate username, validation)
- ✅ User Login (success, invalid credentials, non-existent user)
- ✅ Input Validation (missing fields, password requirements)
- ✅ Database Operations (isolated transactions)

## 🗄️ Database Management

### Alembic Migrations

```bash
# Create a new migration
uv run alembic revision --autogenerate -m "Description of changes"

# Apply migrations
uv run alembic upgrade head

# Downgrade migrations
uv run alembic downgrade -1

# Check migration status
uv run alembic current

# View migration history
uv run alembic history
```

### Database Schema

The application uses SQLModel for defining database schemas with full type safety:

```python
class User(SQLModel, table=True):
    username: str = Field(primary_key=True, index=True)
    password: str = Field(nullable=False, min_length=8)
    client_id: str = Field(nullable=False)
    client_secret: str = Field(nullable=False)
    token_url: str = Field(nullable=False)
    tenant_url: str = Field(nullable=False)
    organization: str = Field(nullable=False)
```

## 📚 API Documentation

### Authentication Endpoints

#### Register User
```http
POST /auth/register
```

**Request Body:**
```json
{
  "username": "string",
  "password": "string",
  "client_id": "string",
  "client_secret": "string",
  "token_url": "string",
  "tenant_url": "string",
  "organization": "string"
}
```

**Response:**
```json
{
  "message": "Registration Successful",
  "username": "string"
}
```

#### Login User
```http
POST /auth/login
```

**Request Body:**
```json
{
  "username": "string",
  "password": "string"
}
```

**Response:**
```json
{
  "message": "Login Successful",
  "username": "string"
}
```

### Interactive API Documentation

When running the server, visit:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## 🏗️ Architecture Patterns

### Service Pattern Implementation

Each module follows a consistent service pattern:

1. **Router Layer**: Handles HTTP requests and responses
2. **Service Layer**: Contains business logic and data validation
3. **Model Layer**: Defines database schemas and relationships
4. **Schema Layer**: Validates request/response data

### Async/Await Pattern

The application is built with async/await throughout:

```python
# Async database operations
async def authenticate_user(username: str, password: str, session: AsyncSession) -> User:
    statement = select(User).where(User.username == username)
    result = await session.execute(statement)
    user = result.scalars().first()
    # ... business logic
    return user

# Async endpoint handlers
@router.post("/login")
async def login(login_req: Login_user_request, session: Session = Depends(get_session)):
    user = await authenticate_user(login_req.username, login_req.password, session)
    return Login_user_response(username=user.username)
```

## 🔧 Development

### Using UV Package Manager

UV provides ultra-fast package management:

```bash
# Add a new dependency
uv add fastapi

# Add a development dependency
uv add --dev pytest

# Remove a dependency
uv remove package-name

# Update dependencies
uv sync

# Run commands in the virtual environment
uv run python script.py
uv run pytest
uv run alembic upgrade head
```

### Code Quality

The project maintains high code quality standards:
- Type hints throughout the codebase
- Pydantic models for data validation
- Comprehensive error handling
- Modular, testable architecture

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests for new functionality
5. Run the test suite (`uv run pytest`)
6. Commit your changes (`git commit -m 'Add amazing feature'`)
7. Push to the branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Links

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLModel Documentation](https://sqlmodel.tiangolo.com/)
- [Alembic Documentation](https://alembic.sqlalchemy.org/)
- [UV Documentation](https://docs.astral.sh/uv/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
