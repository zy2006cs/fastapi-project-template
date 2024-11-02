# FastAPI 项目模板

## 项目信息
- **version：** 1.31
- **name:** FastAPI Project Template

## 项目简介

本项目是一个基于 FastAPI 构建的项目模板，旨在帮助开发者快速启动并构建高效的 Web 应用程序。通过这个模板，您可以轻松实现以下功能：

This project is a FastAPI-based template designed to help developers quickly build efficient web applications. With this template, you can easily implement the following features:

- **Redis 和 MySQL 快速集成**：内置对 Redis 和 MySQL 数据库的支持，只需简单配置即可连接并使用。
  
  **Fast Integration with Redis and MySQL**: Built-in support for Redis and MySQL databases, which can be configured and connected with minimal setup.

- **自动注册路由**：通过遍历指定目录，自动注册 FastAPI 路由，简化了开发过程。
  
  **Automatic Route Registration**: Automatically registers FastAPI routes by scanning specified directories, simplifying the development process.

- **响应数据压缩**：内置 Gzip 中间件，自动压缩响应数据，减少网络传输量，提高响应速度。
  
  **Response Data Compression**: Gzip middleware is included to compress response data automatically, reducing network load and improving response time.

- **浏览器缓存支持**：自动添加缓存控制头部，提高页面加载速度，减少服务器负载。
  
  **Browser Cache Support**: Automatically adds cache-control headers to improve page loading speed and reduce server load.

## 功能特性

### 1. Redis 和 MySQL 快速构建
- **Redis 集成**：通过配置文件，快速连接 Redis，适用于缓存和会话管理等场景（redis-py）。
  
  **Fast Integration with Redis and MySQL**: Quickly connect to Redis by filling in the configuration file, suitable for caching and session management (using `redis-py`).

- **MySQL 集成**：只需在配置文件中填写数据库连接信息，即可快速与 MySQL 数据库进行交互（tortoise-orm）。
  
  **MySQL Integration**: Connect to MySQL with ease by configuring database connection information (using `tortoise-orm`).

- **数据库迁移**：使用 aerich 进行快速的迁移。
  
  **Database Migration**: Fast migrations using `aerich`.

### 2. 自动注册路由 & 请求日志自动记录
- **路径自动注册**：项目自动遍历指定目录，并将其中符合条件的 Python 文件自动注册为 FastAPI 路由，无需手动引入（依赖于 auto_register_routes 方法，需要传入目录路径，其次是接口前缀）。
  
  **Path Auto-Registration**: Automatically registers Python files in specified directories as FastAPI routes, making importing routes easier (dependent on `auto_register_routes`, requiring directory path and route prefix).

- **灵活的路由路径配置**：支持目录嵌套结构的路由自动注册，确保项目结构清晰且易于维护。
  
  **Flexible Route Configuration**: Supports nested directory structures for automatic route registration, ensuring a clear and maintainable project structure.

- **日志功能**：支持自动记录请求信息，用来排除恶意流量。
  
  **Logging**: Automatically records request information to filter malicious traffic.

- **用法讲解**: 1. 使用 FastAPI 原生 `APIRouter` 对象，直接赋值为 `router` 即可 2. 使用封装的 `ServiceRouter` 类自动注册，无需实例化。
  
  **Usage Guide**: 1. Use FastAPI's native `APIRouter` and assign it directly as `router`. 2. Use the encapsulated `ServiceRouter` class for automatic registration without instantiation.

### 3. 数据压缩 & 常规的错误视图处理
- **错误状态码自动处理**：只需要在配置文件设置常用状态码和跳转的 URL 即可实现。
  
  **Automated Error Handling**: Simply set common status codes and redirection URLs in the config file to manage errors.

- **内置 Gzip 支持**：使用 FastAPI 的 Gzip 中间件自动压缩响应数据，适用于大型响应内容的场景。
  
  **Built-in Gzip Support**: Compresses large responses with FastAPI’s Gzip middleware.

- **自定义压缩阈值**：可以通过配置设置压缩的最小数据大小，实现精细化控制。
  
  **Custom Compression Threshold**: Configure a minimum data size for compression to fine-tune performance.

### 4. 浏览器缓存
- **自动缓存控制**：在响应头中自动添加 `Cache-Control`，`ETag` 等缓存控制头部，支持自定义缓存时间。
  
  **Automatic Cache Control**: Adds `Cache-Control`, `ETag`, and other cache control headers to responses, with configurable cache durations.

- **减少服务器负载**：通过缓存机制有效减少重复请求，提高应用的响应性能。
  
  **Server Load Reduction**: Reduces redundant requests, improving response performance through caching.

### 5. 工具类封装
- **OAuth2 认证封装**：提供 JWT 生成，身份鉴权的封装。
  
  **OAuth2 Authentication**: Provides JWT generation and authentication functions.

- **常见加密算法封装**：提供 Base64、Hex、MD5、SHA256、RC4 等常用加密和解密操作的封装。
  
  **Common Encryption Algorithms**: Includes encapsulated methods for Base64, Hex, MD5, SHA256, and RC4 encryption and decryption.

### 6. ServiceRouter
- **ServiceRouter 封装**：封装了各种工具和响应模型方法，包括 JWT 生成和身份认证（auth），旨在通过面向对象的方式进行高质量的代码开发。此封装帮助开发者快速实现常用的 HTTP 请求方法，并简化业务逻辑处理。
  
  **ServiceRouter Encapsulation**: Encapsulates various utility and response model methods, including JWT generation and `auth` authentication, aimed at high-quality code development through object-oriented principles. This helps developers streamline HTTP requests and simplify business logic.

### 7. RESTful API 模型化开发
- **封装 ServiceRouter 方法**：提供 HTTP 常用请求方法：get、post、put、delete，封装响应方法快速处理业务需求。
  
  **Encapsulated `ServiceRouter` Methods**: Provides common HTTP methods (get, post, put, delete) and encapsulates response methods for efficient business processing.

- **路由注册支持**：凡是在 controller 里面使用了 `ServiceRouter`，无需实例化对象，自动注册。
  
  **Route Registration Support**: All classes using `ServiceRouter` in the controller folder are auto-registered.

### 8. 接口权限认证
- **权限实现**：我们封装了基础的权限规则，并提供基础的登录注册接口进行权限认证。首先定义了 open、add、delete、get、put、all 六种规则，通过 description 属性定义规则。
  
  **Permission Implementation**: We provide basic permission rules with login and registration endpoints for access control. Six rules are defined: open, add, delete, get, put, and all, which are specified using the `description` attribute.

  - **open**：申明之后该接口会为所有登录的用户进行放行。
  
    **open**: Allows access for all logged-in users.

  - **add、delete、put、get**：在设计接口时，这四个规则应该按照 RESTful API 进行设计，get 进行读取，delete 进行删除，put 进行更新，add 进行新增。当 description 申明了其中一个会在 permission 表里面进行读取，查看该用户是否有相应的规则。
  
    **add, delete, put, get**: These rules align with RESTful API design, where `get` reads, `delete` deletes, `put` updates, and `add` creates new resources. Specifying one of these rules will check permissions in the `permission` table.

  - **all**：all 规则和 open 一样比较特殊，all 仅单方面用于数据库的存储。一旦在 permission 表里面申明了某个接口路径的 all，该路径将不受到 add、delete、get、put，在接口处申明 all 等于无效。
  
    **all**: Similar to `open`, `all` is for storage in the database only. If an API path has `all` in the `permission` table, it overrides the other rules.

- **权限错误**,当出现权限错误时会引发403错误 err提示权限错误。
  
  **Permission Error**: A 403 error with the message “permission denied” will be raised for unauthorized access.

### 9. 响应规范
- **响应模型**：响应方法位于/core/res.py 所有的错误以及正常响应都应使用此方法进行返回。状态码不为200 不应该直接使用message而是err，如果使用的ServiceRouter进行开发直接使用类中的res方法和/core/res的响应方法为一个。
  
  **Response Models**: Defined in `/core/res.py`, all error and success responses should use these methods. For non-200 status codes, `err` should be used instead of `message`. When using `ServiceRouter`, you can directly use the `res` method in the class, which corresponds to `/core/res` response methods.

### 10. 项目结构
- **项目文件结构**：遵循 RESTful API 设计规范的文件结构，代码更易于维护与扩展。
  
  **Project Structure**: Adheres to RESTful API design principles for easier maintenance and expansion of the code.

