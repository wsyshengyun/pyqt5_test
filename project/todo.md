## todo 
关于命名规范;  见到名字就知道是干什么的?

以下两个条件验证元素是否出现，传入的参数都是元组类型的locator，如(By.ID, ‘kw’)  
顾名思义，一个只要一个符合条件的元素加载出来就通过；另一个必须所有符合条件的元素都加载出来才行  
presence_of_element_located  
presence_of_all_elements_located  
 
以下三个条件验证元素是否可见，前两个传入参数是元组类型的locator，第三个传入WebElement  
第一个和第三个其实质是一样的  
visibility_of_element_located  
invisibility_of_element_located  