const dropArea = document.getElementById("drop-area");
const fileBtn = document.getElementById("file");

dropArea.addEventListener("dragover", (e) => {
  e.preventDefault();
  dropArea.classList.add("dragover");
});

dropArea.addEventListener("dragleave", () => {
  dropArea.classList.remove("dragover");
});

const screenshotPreview = document.getElementById("screenshot-preview");
dropArea.addEventListener("drop", (e) => {
  e.preventDefault();
  screenshotPreview.innerHTML = "";

  dropArea.classList.remove("dragover");

  const files = e.dataTransfer.files;

  const file = files[0];
  console.log(file);
  const appIdMatch = window.location.pathname.match(/\/apps\/(\d)/);
  const appId = appIdMatch ? appIdMatch[1] : null;
  addTask(appId);
  const reader = new FileReader();
  reader.onload = (event) => {
    const img = document.createElement("img");
    img.src = event.target.result;
    screenshotPreview.appendChild(img);
  };
  reader.readAsDataURL(file);
});

fileBtn.onchange = (e) => {
  console.log("bobobob");
  const reader = new FileReader();
  const imgElem = document.createElement("img");
  const appIdMatch = window.location.pathname.match(/\/apps\/(\d)/);
  const appId = appIdMatch ? appIdMatch[1] : null;
  addTask(appId);

  reader.onload = (event) => {
    imgElem.src = event.target.result;
    screenshotPreview.innerHTML = "";
    screenshotPreview.appendChild(imgElem);
  };
  reader.readAsDataURL(e.target.files[0]);
};

function addTask(appId) {
  console.log("add tasks");
  fetch("{% url tasks %}", {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
      "X-CSRFToken": "{{ csrf_token }}",
    },
    body: {
      app_id: appId,
    },
  })
    .then((res) => {
      console.log(res);
    })
    .catch((err) => {
      console.log(err);
    });
}
