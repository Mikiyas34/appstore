const logoInput = document.getElementById("logo-input");
const logoPreview = document.getElementById("logo-preview");
const blankLogo = document.getElementById("blank-logo");

logoInput.onchange = (e) => {
  const reader = new FileReader();
  const imgElem = document.createElement("img");
  reader.onload = (event) => {
    imgElem.src = event.target.result;
    logoPreview.innerHTML = "";
    blankLogo.style.display = "none";
    logoPreview.appendChild(imgElem);
  };
  reader.readAsDataURL(e.target.files[0]);
};
