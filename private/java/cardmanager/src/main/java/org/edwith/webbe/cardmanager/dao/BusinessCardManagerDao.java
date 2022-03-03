package org.edwith.webbe.cardmanager.dao;

import org.edwith.webbe.cardmanager.dto.BusinessCard;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.List;

public class BusinessCardManagerDao {
	private static String dburl = "jdbc:mysql://localhost:3306/project?useSSL=false&serverTimezone=UTC";
	private static String dbUser = "connectuser";
	private static String dbpasswd = "connect123!@#";
	
    public List<BusinessCard> searchBusinessCard(String keyword){
    	List<BusinessCard> list = new ArrayList<>();
    	try{
    		Class.forName("com.mysql.jdbc.Driver");
    	} catch (Exception e) {
			e.printStackTrace();
		}
    	String sql = "select * from businesscard where name like ?";
    	try (Connection conn = DriverManager.getConnection(dburl, dbUser, dbpasswd);
				PreparedStatement ps = conn.prepareStatement(sql)){
    		String k_name = '%'+keyword+'%';
    		ps.setString(1, k_name);
    		try (ResultSet rs = ps.executeQuery()){
				while(rs.next()) {
					String name = rs.getString(1);
					String phone = rs.getString(2);
					String companyname = rs.getString(3);
					BusinessCard bc = new BusinessCard(name, phone, companyname);
					list.add(bc);
				}
			} catch (Exception ex) {
				ex.printStackTrace();
			}
			
		} catch (Exception e) {
			e.printStackTrace();
		}
    	return list;
    	
    }

    public BusinessCard addBusinessCard(BusinessCard businessCard){

    	try{
    		Class.forName("com.mysql.jdbc.Driver");
    	} catch (Exception e) {
			e.printStackTrace();
		}
    	String sql = "insert into businesscard values(?,?,?,?)";
    	try (Connection conn = DriverManager.getConnection(dburl, dbUser, dbpasswd);
    			PreparedStatement ps = conn.prepareStatement(sql)){
			ps.setString(1, businessCard.getName());
			ps.setString(2, businessCard.getPhone());
			ps.setString(3, businessCard.getCompanyName());
			DateFormat df = new SimpleDateFormat("EEE MMM dd hh:mm:ss zzz yyyy");
			ps.setString(4,  df.format(businessCard.getCreateDate()));
			ps.executeUpdate();
		} catch (Exception e) {
			e.printStackTrace();
		}
    	return businessCard;
    }
}
