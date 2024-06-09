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
  const reader = new FileReader();
  reader.onload = (event) => {
    const img = document.createElement("img");
    img.src = event.target.result;
    screenshotPreview.appendChild(img);
  };
  reader.readAsDataURL(file);
});

fileBtn.onchange = (e) => {
  const reader = new FileReader();
  const imgElem = document.createElement("img");
  reader.onload = (event) => {
    imgElem.src = event.target.result;
    screenshotPreview.innerHTML = "";
    screenshotPreview.appendChild(imgElem);
  };
  reader.readAsDataURL(e.target.files[0]);
};
