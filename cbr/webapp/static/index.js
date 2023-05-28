
function displayRecommendedItems(recommendedItems) {

    const recommendedItemsUl = document.getElementById("ul-recommended-items");
    removeAllChildNodes(recommendedItemsUl);

    recommendedItems.forEach((item) => {
     
        const li = document.createElement("li");

        const a = document.createElement("a");
        a.setAttribute("href", item.url);
        a.setAttribute("target", "_blank");
        a.setAttribute("onclick", `viewItem("${item.title}")`);
        a.textContent = item.title;

        li.appendChild(a);
        recommendedItemsUl.appendChild(li);
    });
}

function displayUsername(username) {

    document.getElementById("span-username").textContent = username;
}

function displayUsernames(usernames, userOptionsDivID) {

    const userOptionsDiv = document.getElementById(userOptionsDivID);
    removeAllChildNodes(userOptionsDiv);

    usernames.forEach(username => {
        
        const radioButton = document.createElement("input");
        radioButton.setAttribute("type", "radio");
        radioButton.setAttribute("value", username);
        radioButton.setAttribute("id", "option-" + username);
        radioButton.setAttribute("name", "username");
        radioButton.setAttribute("required", "");
    
        const label = document.createElement("label");
        label.setAttribute("for", "option-" + username);
        label.textContent = username;
    
        userOptionsDiv.appendChild(radioButton);
        userOptionsDiv.appendChild(label);
        userOptionsDiv.appendChild(document.createElement("br"));
    });
}

function displayDefaultPage() {

    displayUsername("N/A");
    sessionStorage.removeItem("currentUser")
    const recommendedItemsUl = document.getElementById("ul-recommended-items");
    removeAllChildNodes(recommendedItemsUl);
}

function openDialog(dialogID) {

    const dialog = document.getElementById(dialogID);
    dialog.showModal();
}

function closeDialog(dialogID) {

    const dialog = document.getElementById(dialogID);
    dialog.close();
}

function removeAllChildNodes(node) {

    while (node.firstChild) {

        node.removeChild(node.firstChild);
    }
}

async function viewItem(itemTitle) {

    const currentUser = sessionStorage.getItem("currentUser");

    try {

        if (!currentUser) {

            throw new Error();
        }

        const data = new FormData();
        data.append("username", currentUser);
        data.append("title", itemTitle);
        
        await fetch("/api/view", { method: "PUT", body: data });

    } catch {

        displayDefaultPage();
    }
}

async function getRecommendedItems() {

    const currentUser = sessionStorage.getItem("currentUser");

    try {

        if (!currentUser) {

            throw new Error();
        }

        const response = await fetch("/api/recommend/" + currentUser);
        const recommendedItems = await response.json();
        displayRecommendedItems(recommendedItems);

    } catch {

        displayDefaultPage();
    }
}

async function getUsernames() {

    const response = await fetch("/api/users");
    return await response.json();
}

async function changeUser() {

    const changeUserForm = document.getElementById("form-change-user");

    try {

        const username = new FormData(changeUserForm).get("username");

        const response = await fetch("/api/users/" + username);
        const recommendedItems = await response.json();

        sessionStorage.setItem("currentUser", username);
        displayRecommendedItems(recommendedItems);
        displayUsername(username);

    } catch {

        displayDefaultPage();
    }

    closeDialog("dialog-change-user");
}

async function deleteUser() {

    const currentUser = sessionStorage.getItem("currentUser");
    const deleteUserForm = document.getElementById("form-delete-user");

    try {

        const username = new FormData(deleteUserForm).get("username");

        await fetch("/api/users/" + username, { method: "DELETE" });

        if (username === currentUser) {

            displayDefaultPage();
        }

    } catch {

        displayDefaultPage();
    }

    closeDialog("dialog-delete-user");
}

async function createUser() {

    const createUserForm = document.getElementById("form-create-user");

    try {

        const username = new FormData(createUserForm).get("username");

        if (!username) {

            throw new Error();
        }

        const response = await fetch("/api/users/" + username, { method: "PUT" });
        const recommendedItems = await response.json();

        sessionStorage.setItem("currentUser", username);
        displayRecommendedItems(recommendedItems);
        displayUsername(username);

    } catch {

        displayDefaultPage();
    }

    closeDialog("dialog-create-user");
}

async function showChangeUserDialog() {

    const usernames = await getUsernames();
    displayUsernames(usernames, "div-change-user-options");
    openDialog("dialog-change-user");
}

async function showDeleteUserDialog() {

    const usernames = await getUsernames();
    displayUsernames(usernames, "div-delete-user-options");
    openDialog("dialog-delete-user");
}

window.addEventListener("load", function() {

    sessionStorage.clear();

    document.getElementById("btn-recommend").addEventListener("click", () => {
        getRecommendedItems();
    });

    // change user dialog

    document.getElementById("btn-show-change-user-dialog").addEventListener("click", () => {
        showChangeUserDialog();
    });

    document.getElementById("btn-close-change-user-dialog").addEventListener("click", () => {
        document.getElementById("dialog-change-user").close();
    });

    // create user dialog

    document.getElementById("btn-show-create-user-dialog").addEventListener("click", () => {
        document.getElementById("dialog-create-user").showModal();
    });

    document.getElementById("btn-close-create-user-dialog").addEventListener("click", () => {
        document.getElementById("dialog-create-user").close();
    });

    // delete user dialog

    document.getElementById("btn-show-delete-user-dialog").addEventListener("click", () => {
        showDeleteUserDialog();
    });

    document.getElementById("btn-close-delete-user-dialog").addEventListener("click", () => {
        document.getElementById("dialog-delete-user").close();
    });

    // form submit

    document.getElementById("form-change-user").addEventListener("submit", (event) => {
        event.preventDefault();
        changeUser();
    });

    document.getElementById("form-create-user").addEventListener("submit", (event) => {
        event.preventDefault();
        createUser();
    });

    document.getElementById("form-delete-user").addEventListener("submit", (event) => {
        event.preventDefault();
        deleteUser();
    });
})