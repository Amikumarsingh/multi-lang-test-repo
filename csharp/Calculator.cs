// C# class with various errors

using System;
using System.Collections.Generic;
using System.Linq;
// Missing: using System.Text;

namespace DataProcessing
{
    public class Calculator
    {
        private List<int> history;
        
        public Calculator()
        {
            history = new List<int>();
        }
        
        // Missing return type - syntax error
        public Add(int a, int b)
        {
            int result = a + b;
            history.Add(result);
            return result;
        }
        
        public int Subtract(int a, int b)
        {
            return a - b;
        }
        
        // Type error: wrong return type
        public string GetCount()
        {
            return history.Count;  // Should return int
        }
        
        // Syntax error: missing semicolon
        public void Clear()
        {
            history.Clear()
        }
        
        // Logic error: wrong condition
        public bool IsEmpty()
        {
            return history.Count > 0;  // Should be == 0
        }
        
        // Missing StringBuilder import
        public string ConcatenateHistory()
        {
            StringBuilder sb = new StringBuilder();
            foreach (var item in history)
            {
                sb.Append(item).Append(" ");
            }
            return sb.ToString();
        }
        
        // Syntax error: missing closing brace
        public double GetAverage()
        {
            if (history.Count == 0)
            {
                return 0;
            }
            return history.Average();
        
    }
}
