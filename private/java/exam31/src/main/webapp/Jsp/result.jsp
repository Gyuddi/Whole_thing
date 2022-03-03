<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<%
int random1 = (int)request.getAttribute("random1");
int random2 = (int)request.getAttribute("random2");
int sum = (int)request.getAttribute("sum");
%>
<%=random1 %> + <%=random2 %> = <%=sum %>
</body>
</html>