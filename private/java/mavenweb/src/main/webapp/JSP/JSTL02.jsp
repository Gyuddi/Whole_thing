<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>

<c:set var = "n" scope = "request" value = "10"/>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<c:if test="${n == 0}">
n은 과 0과 같습니다.
</c:if>
<c:if test="${n==10 }">
n은 10과 같습니다.
</c:if>

</body>
</html>