package kr.or.connect.jdbcexam.dao;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

import kr.or.connect.jdbcexam.dto.Role;

public class RoleDao {
	private static String dburl = "jdbc:mysql://localhost:3306/connectdb?useSSL=false&serverTimezone=UTC";
	private static String dbUser = "connectuser";
	private static String dbpasswd = "connect123!@#";
	
	public int deleteRole(Integer roleid) {
		int deleteCount = 0;
		try {
			Class.forName("com.mysql.jdbc.Driver");
		} catch (ClassNotFoundException e) {
			e.printStackTrace();
		}
		String sql = "delete from role where role_id=?";
		try (Connection conn = DriverManager.getConnection(dburl, dbUser, dbpasswd);
				PreparedStatement ps = conn.prepareStatement(sql)){
			ps.setInt(1, roleid);
			deleteCount = ps.executeUpdate();
		} catch (Exception e) {
			e.printStackTrace();
		}
		return deleteCount;
	}

	public int updateRole(Role role) {
		int updateCount = 0;
		Connection conn = null;
		PreparedStatement ps = null;
		try {
			Class.forName("com.mysql.jdbc.Driver");
			conn = DriverManager.getConnection(dburl, dbUser, dbpasswd);
			String sql = "update role set description=? where role_id=?";
			ps = conn.prepareStatement(sql);
			ps.setString(1, role.getDescription());
			ps.setInt(2, role.getRoleId());
			updateCount = ps.executeUpdate();
		} catch (Exception ex) {
			ex.printStackTrace();
		}finally {
			if (ps != null) {
				try {
					ps.close();
				} catch (SQLException e) {
					e.printStackTrace();
				}
			}
			if (conn != null) {
				try {
					conn.close();
				} catch (SQLException e) {
					e.printStackTrace();
				}
			}
		}
		return updateCount;
	}
	
	
	public int addRole(Role role) {
		int insertCount = 0;
		Connection conn = null;
		PreparedStatement ps = null;
		try {
			Class.forName("com.mysql.jdbc.Driver");
			conn = DriverManager.getConnection(dburl, dbUser, dbpasswd);
			String sql = "insert into role (role_id, description) values(?,?)";
			ps = conn.prepareStatement(sql);
			ps.setInt(1, role.getRoleId());
			ps.setString(2, role.getDescription());
			//insert,update,delete는 ps.executeQuery()가 아닌 ps.executeUpdate();를 사용한다.
			insertCount = ps.executeUpdate();
		} catch (Exception ex) {
			ex.printStackTrace();
		}finally {
			if (ps != null) {
				try {
					ps.close();
				} catch (SQLException e) {
					e.printStackTrace();
				}
			}
			if (conn != null) {
				try {
					conn.close();
				} catch (SQLException e) {
					e.printStackTrace();
				}
			}
		}
		return insertCount;
	}
	
	public Role getRole(Integer roleId) {
		Role role = null;
		Connection conn = null;
		PreparedStatement ps = null;
		ResultSet rs = null;

		try {
			Class.forName("com.mysql.jdbc.Driver");
			conn = DriverManager.getConnection(dburl, dbUser, dbpasswd);
			String sql = "SELECT description,role_id FROM role WHERE role_id = ?";
			ps = conn.prepareStatement(sql);
			ps.setInt(1, roleId);
			rs = ps.executeQuery();

			if (rs.next()) {
				String description = rs.getString(1);
				int id = rs.getInt("role_id");
				role = new Role(id, description);
			}
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			if (rs != null) {
				try {
					rs.close();
				} catch (SQLException e) {
					e.printStackTrace();
				}
			}
			if (ps != null) {
				try {
					ps.close();
				} catch (SQLException e) {
					e.printStackTrace();
				}
			}
			if (conn != null) {
				try {
					conn.close();
				} catch (SQLException e) {
					e.printStackTrace();
				}
			}
		}

		return role;
	}
	
	public List<Role> getRoles() {
		List<Role> list = new ArrayList<>();

		try {
			Class.forName("com.mysql.jdbc.Driver");
		} catch (ClassNotFoundException e) {
			e.printStackTrace();
		}

		String sql = "SELECT description, role_id FROM role order by role_id desc";
		try (Connection conn = DriverManager.getConnection(dburl, dbUser, dbpasswd);
				PreparedStatement ps = conn.prepareStatement(sql)) {

			try (ResultSet rs = ps.executeQuery()) {

				while (rs.next()) {
					String description = rs.getString(1);
					int id = rs.getInt("role_id");
					Role role = new Role(id, description);
					list.add(role); // list에 반복할때마다 Role인스턴스를 생성하여 list에 추가한다.
				}
			} catch (Exception e) {
				e.printStackTrace();
			}
		} catch (Exception ex) {
			ex.printStackTrace();
		}
		return list;
	}
}