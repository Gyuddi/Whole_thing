package org.edwith.webbe.cardmanager;

import java.util.List;

import org.edwith.webbe.cardmanager.dao.BusinessCardManagerDao;
import org.edwith.webbe.cardmanager.dto.BusinessCard;

public class JDBCpractice {
	public static void main(String[] args) {
		BusinessCardManagerDao dao = new BusinessCardManagerDao();
		List<BusinessCard> list = dao.searchBusinessCard("김");
		for(BusinessCard bc:list) {
			System.out.println(bc.toString());
		}
	}

}
