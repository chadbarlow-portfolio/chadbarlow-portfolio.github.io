function drawSunburstChart(sunburstData) {
  anychart.onDocumentReady(function() {
    var data = sunburstData;
    console.log(data);
    var chart = anychart.sunburst(data, 'as-table');
    chart.calculationMode("parent-independent");
    chart
    .leaves()
    .labels()
    .format(function () {
      var label = this.name;
      var value = this.value;
      return `${label} \n ${value}`;
    });
    chart.listen("pointClick", function (event) {
      var point = event.point;
      var films = point.get("films");
      if (films) {
        const cardText = card.querySelector(".card-text");
        cardText.innerHTML = films.join("<br>");
        card.style.display = "block";
        console.log(cardText.innerHTML);
      } else {
        chart.tooltip().title(true);
        chart.tooltip().format("{%name}");
        card.style.display = "none";
      }
    });
    const tooltipContainer = document.getElementById("tooltip-container");
    const card = document.createElement("div");
    card.classList.add("card");
    card.style.width = "18rem";
    const cardBody = document.createElement("div");
    cardBody.classList.add("card-body");
    const cardTitle = document.createElement("h5");
    cardTitle.classList.add("card-title");
    cardTitle.textContent = "Top 10 Films";
    const cardText = document.createElement("p");
    cardText.classList.add("card-text");
    cardBody.appendChild(cardTitle);
    cardBody.appendChild(cardText);
    card.appendChild(cardBody);
    tooltipContainer.appendChild(card);
    chart.radius("30%");
    chart.title("Movies by Platform and Genre");
    chart.container("sunburst-container");
    chart.draw();
  });
}