import org.junit.Test;
import static org.junit.Assert.*;

public class DataManagerTest {
    
    @Test
    public void testProcessData() {
        DataManager dm = new DataManager();
        String result = dm.processData("test");
        assertNotNull(result);
    }
    
    @Test
    public void testValidateInput() {
        DataManager dm = new DataManager();
        assertTrue(dm.validateInput("valid"));
    }
    
    @Test
    public void testCalculateSum() {
        DataManager dm = new DataManager();
        assertEquals(15, dm.calculateSum(5, 10));
    }
}
