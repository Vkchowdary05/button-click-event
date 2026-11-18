/**
 * Lab Project 15: Button Click Event
 * Displays alert message on button click and logs event telemetry.
 */

let clickCount = 0;

/**
 * Handle button click event:
 * 1. Displays alert message
 * 2. Increments counter
 * 3. Records event timestamp
 */
function handleButtonClick() {
  clickCount += 1;

  // Retrieve message from input or use default
  const msgInput = document.getElementById("alert-message-input");
  const message = (msgInput && msgInput.value.trim()) 
    ? msgInput.value.trim() 
    : "DevOps Event Triggered: Button was clicked successfully!";

  // Update DOM elements
  updateDOMOnEvent(message);

  // Trigger browser alert dialog (as required by Question 15.a)
  window.alert(message);

  console.log(`[DevOps Lab 15] Button clicked! Count: ${clickCount}, Message: "${message}"`);
}

/**
 * Update UI telemetry
 */
function updateDOMOnEvent(message) {
  const counterElem = document.getElementById("click-count");
  const timeElem = document.getElementById("last-clicked-time");
  const logList = document.getElementById("event-log-list");

  const now = new Date();
  const timeString = now.toLocaleTimeString();

  if (counterElem) {
    counterElem.textContent = clickCount;
  }

  if (timeElem) {
    timeElem.textContent = `Last Clicked: ${timeString}`;
  }

  if (logList) {
    // Remove empty-log placeholder if present
    const emptyPlaceholder = logList.querySelector(".empty-log");
    if (emptyPlaceholder) {
      emptyPlaceholder.remove();
    }

    const li = document.createElement("li");
    li.className = "log-item";
    li.textContent = `[#${clickCount} at ${timeString}] ${message}`;
    logList.prepend(li);
  }
}

/**
 * Reset click count and telemetry
 */
function resetClickCount() {
  clickCount = 0;
  const counterElem = document.getElementById("click-count");
  const timeElem = document.getElementById("last-clicked-time");
  const logList = document.getElementById("event-log-list");

  if (counterElem) counterElem.textContent = "0";
  if (timeElem) timeElem.textContent = "Last Clicked: None";
  if (logList) {
    logList.innerHTML = '<li class="empty-log">Awaiting first click event...</li>';
  }

  console.log("[DevOps Lab 15] Click counter reset to 0.");
}

// Initial listener setup
document.addEventListener("DOMContentLoaded", () => {
  console.log("[DevOps Lab 15] Button click handler initialized.");
});
