package demo;

import java.io.IOException;
import java.io.PrintWriter;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
@WebServlet("/login")
public class New extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        // Retrieve the parameters from the form
        String name = req.getParameter("name");
        String email = req.getParameter("email");
        // Set content type to HTML
        resp.setContentType("text/html");
        PrintWriter out = resp.getWriter();
        // Send back a response with the submitted data
        out.println("<html><body>");
        out.println("<h1>Form Submitted</h1>");
        out.println("<p><strong>Name:</strong> " + name + "</p>");
        out.println("<p><strong>Email:</strong> " + email + "</p>");
        out.println("</body></html>");
    }
}
