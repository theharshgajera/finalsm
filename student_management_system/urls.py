from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views, Hod_Views, Staff_Views, Student_Views, parent_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.BASE, name='base'),
    path('', views.LOGIN, name='login'),
    path('doLogin', views.doLogin, name='doLogin'),
    path('doLogout', views.doLogout, name='logout'),
    path('Profile', views.PROFILE, name='profile'),
    path('Profile/update', views.PROFILE_UPDATE, name='profile_update'),
    
    # HOD URLs
    path('Hod/Home', Hod_Views.HOME, name='hod_home'),
    path('Hod/Student/Add', Hod_Views.ADD_STUDENT, name='add_student'),
    path('Hod/Student/View', Hod_Views.VIEW_STUDENT, name='view_student'),
    path('Hod/Student/Details/<str:id>', Hod_Views.STUDENT_DETAILS, name='student_details'),  # Add this line
    path('Hod/Student/Edit/<str:id>', Hod_Views.EDIT_STUDENT, name='edit_student'),
    path('Hod/Student/Update', Hod_Views.UPDATE_STUDENT, name='update_student'),
    path('Hod/Student/Delete/<str:admin>', Hod_Views.DELETE_STUDENT, name='delete_student'),
    path('Hod/Staff/Add', Hod_Views.ADD_STAFF, name='add_staff'),
    path('Hod/Staff/View', Hod_Views.VIEW_STAFF, name='view_staff'),
    path('Hod/Staff/Edit/<str:id>', Hod_Views.EDIT_STAFF, name='edit_staff'),
    path('Hod/Staff/Update', Hod_Views.UPDATE_STAFF, name='update_staff'),
    path('Hod/Staff/Delete/<str:admin>', Hod_Views.DELETE_STAFF, name='delete_staff'),
    path('Hod/Parent/Add', Hod_Views.ADD_PARENT, name='add_parent'),
    path('Hod/Parent/View', Hod_Views.VIEW_PARENT, name='view_parent'),
    path('Hod/Parent/Edit/<str:id>', Hod_Views.EDIT_PARENT, name='edit_parent'),
    path('Hod/Parent/Update', Hod_Views.UPDATE_PARENT, name='update_parent'),
    path('Hod/Parent/Delete/<str:admin>', Hod_Views.DELETE_PARENT, name='delete_parent'),
    path('Hod/Course/Add', Hod_Views.ADD_COURSE, name='add_course'),
    path('Hod/Course/View', Hod_Views.VIEW_COURSE, name='view_course'),
    path('Hod/Course/Edit/<str:id>', Hod_Views.EDIT_COURSE, name='edit_course'),
    path('Hod/Course/Update', Hod_Views.UPDATE_COURSE, name='update_course'),
    path('Hod/Course/Delete/<str:id>', Hod_Views.DELETE_COURSE, name='delete_course'),
    path('Hod/Subject/Add', Hod_Views.ADD_SUBJECT, name='add_subject'),
    path('Hod/Subject/View', Hod_Views.VIEW_SUBJECT, name='view_subject'),
    path('Hod/Subject/Edit/<str:id>', Hod_Views.EDIT_SUBJECT, name='edit_subject'),
    path('Hod/Subject/Update', Hod_Views.UPDATE_SUBJECT, name='update_subject'),
    path('Hod/Subject/Delete/<str:id>', Hod_Views.DELETE_SUBJECT, name='delete_subject'),
    path('Hod/Session/Add', Hod_Views.ADD_SESSION, name='add_session'),
    path('Hod/Session/View', Hod_Views.VIEW_SESSION, name='view_session'),
    path('Hod/Session/Edit/<str:id>', Hod_Views.EDIT_SESSION, name='edit_session'),
    path('Hod/Session/Update', Hod_Views.UPDATE_SESSION, name='update_session'),
    path('Hod/Session/Delete/<str:id>', Hod_Views.DELETE_SESSION, name='delete_session'),
    path('Hod/Staff/Send_Notification', Hod_Views.STAFF_SEND_NOTIFICATION, name='staff_send_notification'),
    path('Hod/Staff/save_notification', Hod_Views.SAVE_STAFF_NOTIFICATION, name='save_staff_notification'),
    path('Hod/Student/send_notification', Hod_Views.STUDENT_SEND_NOTIFICATION, name='student_send_notification'),
    path('Hod/Student/save_notification', Hod_Views.SAVE_STUDENT_NOTIFICATION, name='save_student_notification'),
    path('Hod/Staff/Leave_view', Hod_Views.STAFF_LEAVE_VIEW, name='staff_leave_view'),
    path('Hod/Staff/approve_leave/<str:id>', Hod_Views.STAFF_APPROVE_LEAVE, name='staff_approve_leave'),
    path('Hod/Staff/disapprove_leave/<str:id>', Hod_Views.STAFF_DISAPPROVE_LEAVE, name='staff_disapprove_leave'),
    path('Hod/Student/Leave_view', Hod_Views.STUDENT_LEAVE_VIEW, name='student_leave_view'),
    path('Hod/Student/approve_leave/<str:id>', Hod_Views.STUDENT_APPROVE_LEAVE, name='student_approve_leave'),
    path('Hod/Student/disapprove_leave/<str:id>', Hod_Views.STUDENT_DISAPPROVE_LEAVE, name='student_disapprove_leave'),
    path('Hod/Staff/feedback', Hod_Views.STAFF_FEEDBACK, name='staff_feedback_reply'),
    path('Hod/Staff/feedback/save', Hod_Views.STAFF_FEEDBACK_SAVE, name='staff_feedback_reply_save'),
    path('Hod/Student/feedback', Hod_Views.STUDENT_FEEDBACK, name='get_student_feedback'),
    path('Hod/Student/feedback/reply/save', Hod_Views.REPLY_STUDENT_FEEDBACK, name='reply_student_feedback'),
    path('Hod/View/Attendance', Hod_Views.VIEW_ATTENDANCE, name='view_attendance'),
    path('get_subjects_by_course/', Hod_Views.get_subjects_by_course, name='get_subjects_by_course'),

    # Bulk Add URLs
    path('Hod/Student/Bulk_Add', Hod_Views.BULK_ADD_STUDENT, name='bulk_add_student'),
    path('Hod/Staff/Bulk_Add', Hod_Views.BULK_ADD_STAFF, name='bulk_add_staff'),

    # Staff URLs
    path('Staff/Home', Staff_Views.HOME, name='staff_home'),
    path('Staff/Notifications', Staff_Views.NOTIFICATIONS, name='notifications'),
    path('Staff/mark_as_done/<str:status>', Staff_Views.STAFF_NOTIFICATION_MARK_AS_DONE, name='staff_notification_mark_as_done'),
    path('Staff/Apply_leave', Staff_Views.STAFF_APPLY_LEAVE, name='staff_apply_leave'),
    path('Staff/Apply_leave_save', Staff_Views.STAFF_APPLY_LEAVE_SAVE, name='staff_apply_leave_save'),
    path('Staff/Feedback', Staff_Views.STAFF_FEEDBACK, name='staff_feedback'),
    path('Staff/Send/Feedback', Staff_Views.STAFF_SEND_FEEDBACK, name='staff_send_feedback'),
    path('Staff/Take_Attendance', Staff_Views.STAFF_TAKE_ATTENDANCE, name='staff_take_attendance'),
    path('Staff/Save_Attendance', Staff_Views.STAFF_SAVE_ATTENDANCE, name='staff_save_attendance'),
    path('Staff/View_Attendance', Staff_Views.STAFF_VIEW_ATTENDANCE, name='staff_view_attendance'),
    path('Staff/Add_Result/', Staff_Views.STAFF_ADD_RESULT, name='staff_add_result'),
    path('Staff/View_Result/', Staff_Views.STAFF_VIEW_RESULT, name='staff_view_result'),
    path('Staff/Download_Result_Template/', Staff_Views.STAFF_DOWNLOAD_RESULT_TEMPLATE, name='staff_download_result_template'),
    path('Staff/Notes', Staff_Views.STAFF_NOTES, name='staff_notes'),
    path('Staff/Notes/Create', Staff_Views.STAFF_CREATE_NOTE, name='staff_create_note'),
    path('Staff/Notes/Edit/<int:note_id>', Staff_Views.STAFF_EDIT_NOTE, name='staff_edit_note'),
    path('Staff/Notes/Delete/<int:note_id>', Staff_Views.STAFF_DELETE_NOTE, name='staff_delete_note'),

    # Staff Study Materials URLs
    path('staff/study-materials/', Staff_Views.STAFF_STUDY_MATERIALS, name='staff_study_materials'),
    path('staff/add-material/', Staff_Views.STAFF_ADD_MATERIAL, name='staff_add_material'),
    path('staff/delete-material/<int:material_id>/', Staff_Views.STAFF_DELETE_MATERIAL, name='staff_delete_material'),

    # Student URLs
    path('Student/Home', Student_Views.Home, name='student_home'),
    path('Student/Notifications', Student_Views.STUDENT_NOTIFICATION, name='student_notification'),
    path('Student/mark_as_done/<str:status>', Student_Views.STUDENT_NOTIFICATION_MARK_AS_DONE, name='student_notification_mark_as_done'),
    path('Student/feedback', Student_Views.STUDENT_FEEDBACK, name='student_feedback'),
    path('Student/feedback/save', Student_Views.STUDENT_FEEDBACK_SAVE, name='student_feedback_save'),
    path('Student/apply_for_leave', Student_Views.STUDENT_LEAVE, name='student_leave'),
    path('Student/Leave_save', Student_Views.STUDENT_LEAVE_SAVE, name='student_leave_save'),
    path('Student/View_Attendance', Student_Views.STUDENT_VIEW_ATTENDANCE, name='student_view_attendance'),
    path('Student/view_Result', Student_Views.VIEW_RESULT, name='view_result'),
    path('Student/Notes', Student_Views.STUDENT_NOTES, name='student_notes'),
    path('Student/Notes/Create', Student_Views.STUDENT_CREATE_NOTE, name='student_create_note'),
    path('Student/Notes/Edit/<int:note_id>', Student_Views.STUDENT_EDIT_NOTE, name='student_edit_note'),
    path('Student/Notes/Delete/<int:note_id>', Student_Views.STUDENT_DELETE_NOTE, name='student_delete_note'),

    # Student Study Materials URL
    path('student/study-materials/', Student_Views.STUDENT_VIEW_MATERIALS, name='student_view_materials'),
    path('student/doubt-solver/', Student_Views.student_doubt_solver, name='student_doubt_solver'),

    # Parent URLs
    path('Parent/Home', parent_views.HOME, name='parent_home'),
    path('Parent/View_Attendance', parent_views.VIEW_ATTENDANCE, name='parent_view_attendance'),
    path('Parent/View_Result', parent_views.VIEW_RESULT, name='parent_view_result'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)