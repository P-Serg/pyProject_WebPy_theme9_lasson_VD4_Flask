function updateDateTime() {
    const now = new Date();
    const formattedNow = now.getFullYear() + '-' +
                         String(now.getMonth() + 1).padStart(2, '0') + '-' +
                         String(now.getDate()).padStart(2, '0') + ' ' +
                         String(now.getHours()).padStart(2, '0') + ':' +
                         String(now.getMinutes()).padStart(2, '0') + ':' +
                         String(now.getSeconds()).padStart(2, '0');
    document.getElementById("datetime").innerText = formattedNow;
}

setInterval(updateDateTime, 1000);
window.onload = updateDateTime;