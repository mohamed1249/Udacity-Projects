WITH t as (
SELECT CustomerId, SUM(Total) as total_
FROM Invoice
GROUP BY 1
)
SELECT c.FirstName
FROM t
join Customer c
ON c.CustomerId = t.CustomerId
And t.total_ = (
SELECT MAX(total_) 
FROM t);

SELECT c.Email, c.FirstName, c.LastName, g.Name
FROM Customer c
JOIN Invoice i
on c.CustomerId = i.CustomerId
JOIN InvoiceLine il
ON i.InvoiceId = il.InvoiceId
JOIN Track t
ON il.TrackId = t.TrackId
JOIN Genre g
ON t.GenreId = g.GenreId
GROUP by 1
ORDER by 1;


