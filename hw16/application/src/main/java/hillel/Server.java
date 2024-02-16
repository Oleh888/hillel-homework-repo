package hillel;

import com.sun.net.httpserver.HttpServer;
import java.io.IOException;
import java.net.InetSocketAddress;
import java.util.logging.Logger;

public class Server {

  private static final Logger log = Logger.getLogger(Server.class.getName());

  public static void main(String[] args) throws IOException {
    var server = HttpServer.create(new InetSocketAddress(8080), 0);
    server.createContext("/", exchange -> {
      String response = "Hello from demo application!\n";
      exchange.sendResponseHeaders(200, response.length());
      var outputStream = exchange.getResponseBody();
      outputStream.write(response.getBytes());
      outputStream.close();
    });
    server.start();
    log.info("Server is running");
  }
}
