//pages/reverse/reverse.js
//获取应用实例
const app = getApp()

Page({
  data:{
    name: "",
    department: ["请选择", "主席团", "云计算", "网媒组", "固宽组", "无线一", "无线二", "秘书处", "新媒体"],
    reason: ["请选择", "小组开会", "活动排练", "学习交流"],
    date: "2018-01-01",
    startTime: "19:00",
    endTime: "23:00",
    index1: 0,
    index2: 0,
  },
  nameChange:function(e){
    this.setData({
      name: e.detail.value
    });
  },
  departmentChange:function(e){
    this.setData({
      index1: e.detail.value
    });
  },
  reasonChange: function (e) {
    this.setData({
      index2: e.detail.value
    });
  },
  dateChange: function (e) {
    this.setData({
      date: e.detail.value
    });
  },
  startTimeChange: function (e) {
    this.setData({
      startTime: e.detail.value
    });
  },
  endTimeChange: function (e) {
    this.setData({
      endTime: e.detail.value
    });
  },
  submit: function (e) {
    //确实很鸡肋啊
    let index1 = this.data.index1;
    let index2 = this.data.index2;
    let name = this.data.name;
    let department = this.data.department[index1];
    let reason = this.data.reason[index2];
    let date = this.data.date;
    let startTime = this.data.startTime;
    let endTime = this.data.endTime; 
    if(name=="" || department=="请选择" ||reason=="请选择"){
      wx.showModal({
        title:"信息有误",
        content:"请重新核对预约信息",
      })
    }else{
      let info = {
        name: name, 
        department: department, 
        reason: reason,
        date: date, 
        startTime: startTime, 
        endTime: endTime
      };
      wx.getStorage({
        key: "reserveInfo",
        success: function(res) {
          let reserveInfo = res.data;
          let i = reserveInfo.length;
          reserveInfo[i] = info;
          wx.setStorage({
            key: "reserveInfo",
            data: reserveInfo,
            success: function (res) {
              console.log(reserveInfo);
            }
          });
          wx.navigateTo({
            url: "../result/result"
          });
          wx.showToast({
            title: "预约成功",
            icon: "success",
            duration: 1000
          });
        },
        fail: function(res) {
          let reserveInfo = [info];
          wx.setStorage({
            key: "reserveInfo",
            data: reserveInfo,
            success: function (res) {
              console.log(reserveInfo);
            }
          });
          wx.navigateTo({
            url: "../result/result"
          });
          wx.showToast({
            title: "预约成功",
            icon: "success",
            duration: 1000
          });
        }
      })
    }
  }
})