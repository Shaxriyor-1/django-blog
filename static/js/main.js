console.log('hello')

const deleteModalButtons = [...document.getElementsByClassName("del-modal-button")]
const deleteBlogBtn = document.getElementById("delete-post-button")
const modalTitle = document.getElementById("modal-title")

deleteModalButtons.forEach(deleteModalButton => deleteModalButton.addEventListener("click", () => {
    const pk = deleteModalButton.getAttribute("data-pk")
    const title = deleteModalButton.getAttribute("data-title")
    deleteBlogBtn.href = `${window.location.origin}/blog_delete/${pk}/`
    modalTitle.innerHTML = `Do you really want to delete post "${title}"?`
}))

const avatarUrl = $("#submit-btn").attr("data-avatar-url")
$("#avatar-input").parent().attr('id', 'avatar-p');
$("#avatar-p").append(`<div class="mt-3">Current: <img 
        class="rounded-circle img-fluid" 
        style="width: 150px;" 
        src='${avatarUrl}'/>
        </div>`)

