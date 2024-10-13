// remove required attribute from all fields
document.addEventListener("DOMContentLoaded", function () {
  const form = document.querySelector("form");
  if (form) {
    const requiredFields = form.querySelectorAll("input[required], textarea[required]");
    requiredFields.forEach((field) => {
      field.removeAttribute("required");
    });
  }
});

// Green alert close after 5 seconds
document.addEventListener("DOMContentLoaded", function () {
  var alerts = document.querySelectorAll(".alert");
  alerts.forEach(function (alert) {
    setTimeout(function () {
      var bsAlert = new bootstrap.Alert(alert);
      bsAlert.close();
    }, 5000);
  });
});

// Function to remove alerts
function removeAlert(alert) {
  alert.style.opacity = "0";
  alert.style.height = "0";
  alert.style.margin = "0";
  alert.style.padding = "0";
  setTimeout(function () {
    alert.remove(); // Completely remove the element from DOM

    // Check if the container is empty and remove it if so
    var container = document.querySelector(".messages-container");
    if (container && container.children.length === 0) {
      container.remove();
    }
  }, 300);
}

// animated text on home page
document.addEventListener("DOMContentLoaded", function () {
  if (!localStorage.getItem("visited")) {
    document.querySelector(".hero-text").classList.add("animate-text");
    localStorage.setItem("visited", "true");
  }

  // Handling alerts
  var alerts = document.querySelectorAll(".system-messages");
  alerts.forEach(function (alert) {
    setTimeout(function () {
      removeAlert(alert);
    }, 5000);

    // Add handling for the close button
    var closeButton = alert.querySelector(".btn-close");
    if (closeButton) {
      closeButton.addEventListener("click", function () {
        removeAlert(alert);
      });
    }
  });

  // Handle closing of system messages
  const messages = document.querySelectorAll(".system-messages");
  messages.forEach((message) => {
    const closeBtn = message.querySelector(".btn-close");
    closeBtn.addEventListener("click", function () {
      message.classList.add("hiding");
      setTimeout(() => {
        message.remove();
      }, 500);
    });
  });
});

document.addEventListener("DOMContentLoaded", function () {
  const carSelect = document.querySelector("select[name='car']");
  const carCardContainer = document.getElementById("car-card-container");

  function updateCarCard(data) {
    carCardContainer.innerHTML = `
      <div class="card-container fade-in">
        <div class="card mb-4 shadow-sm">
          ${
            data.image
              ? `<div class="image-box"><img src="${data.image}" class="card-img-top" alt="${data.brand} ${data.model}"></div>`
              : ""
          }
          <div class="card-body">
            <h5 class="card-title">${data.brand} ${data.model}</h5>
            <p class="card-text">Year: ${data.year}</p>
            <p class="card-text">Category: ${data.category}</p>
            <p class="card-text">Mileage: ${data.mileage} km</p>
            <p class="card-text">Engine Size: ${data.engine_size} L</p>
            <p class="card-text">Fuel: ${data.fuel}</p>
            <p class="card-text">Gearbox: ${data.gearbox}</p>
            <p class="card-text">Air Condition: ${data.air_contidion ? "Yes" : "No"}</p>
            <p class="card-text">Seats: ${data.number_of_seats}</p>
            <p class="card-text">Doors: ${data.number_of_doors}</p>
            <p class="card-text">Color: ${data.color}</p>
            <p class="card-text">Body Style: ${data.body_style}</p>
            <p class="card-text">Availability: ${data.availability ? "Available" : "Not Available"}</p>
          </div>
        </div>
      </div>
    `;
  }

  if (carSelect) {
    carSelect.addEventListener("change", function () {
      const carId = carSelect.value;
      if (carId) {
        fetch(`/api/car/${carId}/`)
          .then((response) => response.json())
          .then((data) => {
            updateCarCard(data);
          });
      } else {
        carCardContainer.innerHTML = "";
      }
    });

    // Trigger the change event to load the initial car card
    const initialCarId = carSelect.value;
    if (initialCarId) {
      fetch(`/api/car/${initialCarId}/`)
        .then((response) => response.json())
        .then((data) => {
          updateCarCard(data);
        });
    }
  }
});
