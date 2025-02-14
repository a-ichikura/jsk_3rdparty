cmake_minimum_required(VERSION 2.8.3)
project(nfc_ros)

find_package(catkin REQUIRED COMPONENTS
    message_generation
    catkin_virtualenv
)

catkin_python_setup()

add_message_files(
  FILES
  NDEFRecord.msg
  Tag.msg
)

generate_messages()

catkin_package(
  CATKIN_DEPENDS message_runtime
)

if ("$ENV{ROS_DISTRO}" MATCHES "indigo")
    message(WARNING "nfc_ros requires python3.6 or newer. For indigo, virtualenv generation is skipped.")
else()
catkin_generate_virtualenv(
    PYTHON_INTERPRETER python3
    CHECK_VENV FALSE
)
catkin_install_python(PROGRAMS
  node_scripts/nfc_ros_node.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(FILES requirements.txt
    DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
endif()
