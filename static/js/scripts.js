var updateBtns = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBtns.length; i++) {
  updateBtns[i].addEventListener('click', () => {
    var productId = this.DataTransferItem.product
    var action = this.DataTransferItem.action
    console.log('productId:', productId, 'Action:', action)
  })
}