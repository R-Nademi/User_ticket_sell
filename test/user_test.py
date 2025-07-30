from controller.user_controller import UserController
user_controller = UserController()



status, message = user_controller.save("ahmad", "ahmadi", "akbar112",
                                       "ali123", "employee", 1)



