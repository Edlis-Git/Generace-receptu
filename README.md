#CZ

##Anotace:
Webová aplikace, která umožní uživatelovi zadat ingredience, objem či kvantitu ingrediencí, shodu vyhledání v závislosti na ingrediencích a kategorií receptu program vrátí jídla a postupy jak je uvařit, které splňují zadání, z velkého množství receptů v databázi.

##Nasazení aplikace:
Aplikace je aktuálně nasazena na AWS a běží na backendovém serveru postaveném pomocí Node.js a Express.js. Data o receptech jsou ukládána v MySQL databázi, která je hostována na EC2 instanci. Backend poskytuje jednoduchý REST API, které má zatím pouze GET end pointy. Tento backend zpracovává požadavky uživatelů, filtruje recepty podle ingrediencí a kategorií a vrací odpovídající výsledky. Díky této architektuře je systém flexibilní, škálovatelný a připravený na budoucí rozšíření, například o personalizovaná doporučení nebo vylepšenou správu uživatelských preferencí. Nutné dodat, že aplikace není dokončena a né vše funcke jsou implementovány.

----------------------------------------------

#EN

##Annotation:
A web application that allows users to input ingredients, the quantity or volume of ingredients, and specify matching criteria based on ingredients and recipe categories. The program then returns meals and cooking instructions that meet the specified requirements, selected from a large number of recipes stored in a database.

##Application Deployment:
The application is currently deployed on AWS and runs on a backend server built using Node.js and Express.js. Recipe data is stored in a MySQL database hosted on an EC2 instance. The backend provides a simple REST API, which currently includes only GET endpoints. This backend processes user requests, filters recipes based on ingredients and categories, and returns the appropriate results. Thanks to this architecture, the system is flexible, scalable, and ready for future enhancements, such as personalized recommendations or improved user preference management. It is important to note that the application is not yet complete and not all features have been implemented.
