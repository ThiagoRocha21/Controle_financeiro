package DB;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

public class SQLiteConnection {
    // conecta ao banco já existente
    public static String Connection(){
        //Url do BD (cria um novo se não existir)
        String DB_URL = "jdbc:sqlite:finances.db";

        String createTableProduct = "CREATE TABLE IF NOT EXISTS produtos ("+
                                "id INTEGER PRIMARY KEY AUTOINCREMENT,"+
                                "name VARCHAR (30),"+
                                "quantidade INTEGER"+
                                ")";

        String createTableFinancial = "CREATE TABLE IF NOT EXISTS financeiro ("+
                                    "id INTEGER PRIMARY KEY AUTOINCREMENT,"+
                                    "preco_unitario FLOAT,"+
                                    "preco_total FLOAT,"+
                                    "produto_id INTEGER,"+
                                    "FOREIGN KEY (produto_id) REFERENCES produtos (id)"+
                                    ")";


        String createTableFinalProduct = "CREATE TABLE IF NOT EXISTS produto_final ("+
                                         "produto_final_id INTEGER PRIMARY KEY AUTOINCREMENT,"+
                                         "nome_produto_final VARCHAR (20),"+
                                         "quantidade INTEGER,"+
                                         "preco FLOAT"+
                                         ")";


        try{
            Class.forName("org.sqlite.JDBC");
            Connection conn = DriverManager.getConnection(DB_URL); Statement stmt = (conn.createStatement());
            //CRIA A TABELA PRODUCT
            stmt.execute(createTableProduct);
            //CRIA A TABELA FINANCIAL
            stmt.execute(createTableFinancial);
            //CRIA A TABELA FinalProduct
            stmt.execute(createTableFinalProduct);
            return "Tabela criada com sucesso✅ ou Conexão estabelecida com sucesso ✅";

        } catch (Exception e) {
            return "Erro: "+e.getMessage();
        }
    }




}
