Select 'High Salary' as category, count(case when income>50000 then 1 end) as accounts_count from Accounts
union all
Select 'Low Salary' as category, count(case when income<20000 then 1 end) as accounts_count from Accounts
union all
Select 'Average Salary' as category, count(case when income between 20000 and 50000  then 1 end) as accounts_count from Accounts

