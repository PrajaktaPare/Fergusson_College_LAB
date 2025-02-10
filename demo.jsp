<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>User Login Form</title>
</head>
<body>
    <h1>User Login</h1>
    <form action="login" method="get">
        <input type="text" name="name" placeholder="Enter your name" required><br>
        <input type="email" name="email" placeholder="Enter your email" required><br><br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
