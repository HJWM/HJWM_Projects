//pages/login/login.js
//获取应用实例
const app = getApp()

Page({
  data:{
    radioValue: [
      { department: "主席团", id: "zxt", isSelect: true },
      { department: "云计算", id: "yjs", isSelect: false },
      { department: "网媒组", id: "wmz", isSelect: false },
      { department: "固宽组", id: "gkz", isSelect: false },                 
      { department: "无线一", id: "wx1", isSelect: false },
      { department: "无线二", id: "wx2", isSelect: false },
      { department: "秘书处", id: "msc", isSelect: false },
      { department: "新媒体", id: "xmt", isSelect: false }
    ]
  },
  radioSelect: function(e){
    //与data-id绑定，有待进一步了解
    let selectId = e.target.dataset.id;
    for(let i=0; i<this.data.radioValue.length; ++i){
      if(this.data.radioValue[i].id == selectId){
        this.data.radioValue[i].isSelect=true;
        let department=this.data.radioValue[i].department;
        //app.js中定义的全局变量v1,好折腾啊好折腾，而且好丑啊好丑
        getApp().globalData.department1=department;
        //console.log(department);
      }else{
        this.data.radioValue[i].isSelect=false;
      }
    }
    this.setData({
      radioValue: this.data.radioValue,
    })
  },
  //获取部门、姓名数据
  formSubmit: function(e){
    let name = e.detail.value.name;
    let department = getApp().globalData.department1;
    if(name == ""){
      wx.showToast({
        title: "姓名不得为空！",
        icon: "none"
      })
    } else {
      var userInfo = {
        name: name,
        department: department
      }
      wx.setStorage({
        key: "userInfo",
        data: userInfo,
        success: function (res) {
          wx.navigateTo({
            url: "../result/result"
          })
        }
      })
    }
  }
})