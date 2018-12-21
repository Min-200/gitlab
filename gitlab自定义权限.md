# 本文主要讲如何修改gitlab默认的权限

场景: 在项目中默认的Main角色，拥有合并代码、修改项目设置、添加人员的权限。
			最终我想实现Main角色只能合并代码，去掉其他权限

vim /opt/gitlab/embedded/service/gitlab-rails/app/policies/project_policy.rb
下图1为 所有者的权限 前4个enable意思是拥有guest、reporter、developer、maintainer4个角色的所有权限


![图1](https://github.com/shiminde/gitlab/blob/master/image/owner.png)
![](https://github.com/shiminde/gitlab/blob/master/image/reporter.png)
![](https://github.com/shiminde/gitlab/blob/master/image/developer.png)
![图5](https://github.com/shiminde/gitlab/blob/master/image/maintainer.png)
![](https://github.com/shiminde/gitlab/blob/master/image/guest.png)


例如： 我现在不想让maintainer_access添加人员和修改项目信息，我在图5中注释掉 
```
gitlab-ctl reconfigure 
gitlab-ctl restart
```
即可
      
# 注意:注释的权限要在owner的规则中添加上，否则owner也会失去相应的权限，因为owner的权限是包含这些定义的权限的
![](https://github.com/shiminde/gitlab/blob/master/image/111.png)
![](https://github.com/shiminde/gitlab/blob/master/image/222.png)

# 修改前
![](https://github.com/shiminde/gitlab/blob/master/image/333.png)
# 修改后
![](https://github.com/shiminde/gitlab/blob/master/image/444.png)
