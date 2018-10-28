//index.js
//获取应用实例
const app = getApp()
Page({
  data:{
    mode:'aspectFit',
    src:'../../public/imag/huawei.png',
    primarySize:'default',
    loading:false,
    plain:false,
    disabled:false,
  },
  showInfo(){
    wx.navigateTo({
      url:'/pages/showInfo/showInfo',
    })
  }
})
