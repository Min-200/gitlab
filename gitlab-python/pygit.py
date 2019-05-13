#!/usr/bin/python
#!coding=utf8
import gitlab
import time

class Git:
        def __init__(self):
                self.url = 'http://gitlab.com'
                self.private_token  = 'nRasdasdzxczxc@#'
        def Auth(self):
                self.gl = gitlab.Gitlab(self.url, private_token=self.private_token)
	def Project_list(self):
		#输出了 项目名称，项目ID，项目URL，创建者ID
		self.projects = self.gl.projects.list(all=True)
		for project in self.projects:
        		print project.name,project.id,project.http_url_to_repo,project.creator_id
	def Project_create(self,group_name,project_name):
		#在组内创建分支
		groups = self.gl.groups.list()
		group_id=""

		for i in groups:
			if i.full_path == group_name:
				group_id = i.id
				project = self.gl.projects.create({'name': project_name, 'namespace_id': group_id},initialize_with_readme="true")
				
				branches = project.branches.list()
				branch = project.branches.create({'branch': 'dev',
                                  'ref': 'master'})
				branch.protect(developers_can_push=True, developers_can_merge=True)
				
				print "OK"
	def Group_list(self):
		groups = self.gl.groups.list()
		for i in groups:
			print i.full_path,i.id
	def Search_group_id(self):
		groups = self.gl.groups.list()
		for i in groups:
	#		if i.full_path == "QA":
				#print i.full_path,i.id
			print i
	
	def User_list(self):
		users = self.gl.users.list()
		for i in users:
			print i
	def User_create(self):
		user = self.gl.users.create({'email': '984570656@qq.com',
                        'username': 'smd',
                        'name': 'smd'},reset_password='true')
		print "OK"


def CreateProject():
	group_name = raw_input("请输入组名:")
	project_name = raw_input("请输入项目名:")
	obj.Project_create(group_name,project_name)

if __name__=="__main__":
	obj = Git()
	obj.Auth()
	#CreateProject()
	obj.User_create()

