const API =
"http://localhost:8000";

async function login(){

const response =
await fetch(
`${API}/login`,
{
method:"POST",
headers:{
"Content-Type":
"application/json"
},
body:JSON.stringify({
username:
document
.getElementById("username")
.value,

password:
document
.getElementById("password")
.value
})
}
);

const data =
await response.json();

localStorage.setItem(
"token",
data.access_token
);

window.location =
"dashboard.html";
}