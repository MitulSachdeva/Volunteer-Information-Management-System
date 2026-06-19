const API =
"http://localhost:8000";

document
.getElementById("volunteerForm")
.addEventListener(
"submit",
async (e)=>{

e.preventDefault();

const formData =
new FormData(e.target);

const data =
Object.fromEntries(
formData.entries()
);

await fetch(
`${API}/volunteers`,
{
method:"POST",
headers:{
"Content-Type":
"application/json"
},
body:JSON.stringify(data)
}
);

alert("Registered!");
});