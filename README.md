# FastAPI Project Template

## 项目信息
- **version：** 1.31
- **name:** FastAPI Project Template

## 项目简介

本项目是一个基于 FastAPI 构建的项目模板，旨在帮助开发者快速启动并构建高效的 Web 应用程序。通过这个模板，您可以轻松实现以下功能：

This project is a template built with FastAPI, designed to help developers quickly start and build efficient web applications. With this template, you can easily achieve the following features:

- **Redis 和 MySQL 快速集成**：内置对 Redis 和 MySQL 数据库的支持，只需简单配置即可连接并使用。
- **Rapid integration of Redis and MySQL**: Built-in support for Redis and MySQL databases, requiring only simple configuration for connection and usage.
- **自动注册路由**：通过遍历指定目录，自动注册 FastAPI 路由，简化了开发过程。
- **Automatic route registration**: Automatically registers FastAPI routes by traversing specified directories, simplifying the development process.
- **响应数据压缩**：内置 Gzip 中间件，自动压缩响应数据，减少网络传输量，提高响应速度。
- **Response data compression**: Built-in Gzip middleware automatically compresses response data to reduce network transmission volume and improve response speed.
- **浏览器缓存支持**：自动添加浏览器缓存控制头部，提升页面加载速度，减少服务器负载。
- **Browser cache support**: Automatically adds browser cache control headers to improve page load speed and reduce server load.

## 功能特性

### 1. Redis 和 MySQL 快速构建
- **Redis 集成**：通过配置文件，快速连接 Redis，适用于缓存和会话管理等场景（redis-py）。
- **MySQL 集成**：只需在配置文件中填写数据库连接信息，即可快速与 MySQL 数据库进行交互（tortoise-orm）。
- **Database migration**: 使用 aerich 进行快速的迁移。

### 2. 自动注册路由 & 请求日志自动记录
- **路径自动注册**：项目自动遍历指定目录，并将其中符合条件的 Python 文件自动注册为 FastAPI 路由，无需手动引入（依赖于 `auto_register_routes` 方法，需要传入目录路径，其次是接口前缀）。
- **Flexible route path configuration**: Supports automatic registration of routes with nested directory structures, ensuring a clear and maintainable project structure.
- **日志功能**：支持自动记录请求信息，用来排除恶意流量。
- **Usage explanation**: 1. 使用 FastAPI 原生 `APIRouter` 对象，直接赋值为 `router` 即可；2. 使用封装的 `ServiceRouter` 类自动注册，无需实例化。

### 3. 数据压缩 & 常规的错误视图处理
- **错误状态码自动处理**：只需要在配置文件设置常用状态码和跳转的 URL 即可实现。
- **内置 Gzip 支持**：使用 FastAPI 的 Gzip 中间件自动压缩响应数据，适用于大型响应内容的场景。
- **自定义压缩阈值**：可以通过配置设置压缩的最小数据大小，实现精细化控制。

### 4. 浏览器缓存
- **自动缓存控制**：在响应头中自动添加 `Cache-Control`，`ETag` 等缓存控制头部，支持自定义缓存时间。
- **减少服务器负载**：通过缓存机制有效减少重复请求，提高应用的响应性能。

### 5. 工具类封装
- **OAuth2 认证封装**：提供 JWT 生成，身份鉴权的封装。
- **Common encryption algorithm encapsulation**: 提供 Base64、Hex、MD5、SHA256、RC4 等常用加密和解密操作的封装。

### 6. ServiceRouter
- **ServiceRouter 封装**：封装了各种工具和响应模型方法，包括 JWT 生成和身份认证（auth），旨在通过面向对象的方式进行高质量的代码开发。此封装帮助开发者快速实现常用的 HTTP 请求方法，并简化业务逻辑处理。

### 7. RESTful API 模型化开发
- **封装 ServiceRouter 方法**：提供 HTTP 常用请求方法：GET、POST、PUT、DELETE，封装响应方法快速处理业务需求。
- **路由注册支持**：凡是在控制器里面使用了 ServiceRouter，无需实例化对象，自动注册。

### 8. 接口权限认证
- **权限实现**：我们封装了基础的权限规则，并提供基础的登录注册接口进行权限认证。首先定义了 open、add、delete、get、put、all 六种规则，通过 description 属性定义规则。
  - **open**：声明之后该接口会为所有登录的用户进行放行。
  - **add、delete、put、get**：在设计接口时，这四个规则应该按照 RESTful API 进行设计。
  - **all**：仅用于数据库存储。
- **权限错误**: 当出现权限错误时会引发403错误，并提示权限错误。

### 9. 响应规范
- **响应模型**: 响应方法位于 `/core/res.py`，所有的错误以及正常响应都应使用此方法进行返回。

## 规则讲解

如下图我们对 UserRouter 类 userinfo 路径进行了规则申明为 get。首先会从 permission 表进行读取，判断用户权限。

![代码预览](demo.png)

## 更新说明
### 1. 我们将在后续的版本围绕 ServiceRouter 对象进行大力整合。
### 2. 后续版本将逐步实现带接口认证的功能。

## 快速开始

### 1. 克隆项目

```bash
git clone https://github.com/zy2006cs/fastapi-project-template.git
cd fastapi-project-template
```
### 2.环境配置
```bash
pip install -r requirements.txt
python app.py
```