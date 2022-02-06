-- StudentId: chahf004
-- FullName: Harold Chandler
-- Question Number: Q1001
-- Question: Products come in various colours.  List the colours of the various products and the number of products for each 
-- of those colours if there are at least 10 items that came in that colour.  Where the colour is not specified, display N/A.

SELECT ISNULL(pro.Color, 'N/A') AS Color, COUNT (Distinct pro.ProductID) AS Count_Of_Products FROM Production.Product pro GROUP BY pro.Color HAVING COUNT(Distinct pro.ProductID) >= 10 Order by Count_Of_Products desc;