const https = require("http");

function fetchDataFromApi() {
  const apiUrl = "http://194.163.167.131:6543/api/v1/candidates/all";

  // Make a GET request to the API
  https
    .get(apiUrl, (response) => {
      let data = "";

      // A chunk of data has been received.
      response.on("data", (chunk) => {
        data += chunk;
      });

      // The whole response has been received.
      response.on("end", () => {
        try {
          const jsonData = JSON.parse(data);
          console.log("Fetched data:", jsonData);
        } catch (error) {
          console.error("Error parsing JSON:", error);
        }
      });
    })
    .on("error", (error) => {
      console.error("Error fetching data:", error);
    });
}

// Set the interval to fetch data every 5 seconds (adjust as needed)
while(true){
  fetchDataFromApi()
}
// To stop fetching after a certain duration (e.g., 30 seconds), you can use setTimeout
// const stopFetchingAfter = setTimeout(() => clearInterval(fetchInterval), 30000);
