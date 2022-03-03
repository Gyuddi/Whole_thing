package kr.or.connect.jdbcexam;

import kr.or.connect.jdbcexam.dao.RoleDao;

public class JDBCExam5 {
	public static void main(String[] args) {
		int roleid = 500;
		RoleDao dao = new RoleDao();
		int deleteCount = dao.deleteRole(roleid);
		System.out.println(deleteCount);
	}
}
