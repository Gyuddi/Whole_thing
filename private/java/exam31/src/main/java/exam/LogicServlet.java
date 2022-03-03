package exam;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class LogicServlet
 */
@WebServlet("/LogicServlet")
public class LogicServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public LogicServlet() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#service(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		int random1 = (int)(Math.random()*100)+1;
		int random2 = (int)(Math.random()*100)+1;
		int sum = random1+random2;
		request.setAttribute("random1", random1);
		request.setAttribute("random2", random2);
		request.setAttribute("sum", sum);
		//Servelt에서 Jsp로.
		//Jsp가 폴더 아래 있을경우 디랙토리를 명시해줘야 한다.
		RequestDispatcher requestDispatcher = request.getRequestDispatcher("/Jsp/result.jsp");
		requestDispatcher.forward(request, response);
	}

}
