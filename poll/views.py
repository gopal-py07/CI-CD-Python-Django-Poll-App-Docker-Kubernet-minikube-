from django.shortcuts import render,get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse
from .forms import PollAddForm, EditPollForm, ChoiceAddForm
from django.db.models import Count
from django.contrib.auth.decorators import login_required



# Create your views here.
from .models import *


# def index(request):
#     all_questions = Poll.objects.order_by('-pub_date')[:5]
#     context = {'all_questions': all_questions}
#     return render(request, 'index.html', context)

@login_required()
def detailview(request, p_id):
    
    poll = get_object_or_404(Poll, id=p_id)
    
    loop_count = poll.choice_set.count()
    print(loop_count)
    context = {
        'poll': poll,
        'loop_time': range(0, loop_count),
    }
    return render(request, 'polls/detail.html', context)

@login_required()
def create_Poll(request):
        if request.method == 'POST':
            form = PollAddForm(request.POST)
            if form.is_valid:
                poll = form.save(commit=False)
                poll.owner = request.user
                poll.save()
                new_choice1 = Choice(
                    poll=poll, choice_text=form.cleaned_data['choice1']).save()
                new_choice2 = Choice(
                    poll=poll, choice_text=form.cleaned_data['choice2']).save()

                messages.success(
                    request, "Poll & Choices Created successfully.", extra_tags='alert alert-success alert-dismissible fade show')

                return redirect('polls:list')
        else:
            form = PollAddForm()
            context = {
                'form': form,
            }
            return render(request, 'polls/create_poll.html', context)

@login_required()
def list_poll(request):
    
    all_polls = Poll.objects.all()  
    print(all_polls)
    context = {
        'polls': all_polls
    }
    return render(request, 'polls/poll_list.html', context)

@login_required()
def vote(request, p_id):
    poll = get_object_or_404(Poll, pk=p_id)
    choice_id = request.POST.get('choice')
    
    if choice_id:
        choice = Choice.objects.get(id=choice_id)
        vote = Vote(user=request.user, poll=poll, choice=choice)
        vote.save()

        return render(request, 'polls/result.html', {'poll': poll})
    else:
        messages.error(
            request, "No choice selected!", extra_tags='alert alert-warning alert-dismissible fade show')
        return redirect("polls:detail", p_id)
    
    
    
def edit_poll(request, p_id):
    
    poll_instance = get_object_or_404(Poll, pk=p_id)
    
    if request.method == 'POST':
        form = EditPollForm(request.POST, instance=poll_instance)
        if form.is_valid:
            form.save()
            messages.success(request, "Poll Updated successfully.",
                             extra_tags='alert alert-success alert-dismissible fade show')
            return redirect("polls:list")
            #return redirect('list')

    else:
        form = EditPollForm(instance=poll_instance)

    return render(request, "polls/edit_poll.html", {'form': form, 'poll': poll_instance})

@login_required()
def polls_delete(request, p_id):
    poll = get_object_or_404(Poll, pk=p_id)
    if request.user != poll.owner:
        return redirect('home')
    poll.delete()
    messages.success(request, "Poll Deleted successfully.",
                     extra_tags='alert alert-success alert-dismissible fade show')
    return redirect("polls:list")

@login_required
def add_choice(request, p_id):
    poll = get_object_or_404(Poll, pk=p_id)

    if request.method == 'POST':
        form = ChoiceAddForm(request.POST)
        if form.is_valid:
            new_choice = form.save(commit=False)
            new_choice.poll = poll
            new_choice.save()
            messages.success(
                request, "Choice added successfully.", extra_tags='alert alert-success alert-dismissible fade show')
            return redirect('polls:editPoll', poll.id)
    else:
        form = ChoiceAddForm()
    context = {
        'form': form,
    }
    return render(request, 'polls/add_choice.html', context)



@login_required
def choice_edit(request, choice_id):
    choice = get_object_or_404(Choice, pk=choice_id)
    poll = get_object_or_404(Poll, pk=choice.poll.id)
    
    if request.method == 'POST':
        form = ChoiceAddForm(request.POST, instance=choice)
        if form.is_valid:
            new_choice = form.save(commit=False)
            new_choice.poll = poll
            new_choice.save()
            messages.success(
                request, "Choice Updated successfully.", extra_tags='alert alert-success alert-dismissible fade show')
            print(poll.id)
            return redirect('polls:editPoll', poll.id)
    else:
        form = ChoiceAddForm(instance=choice)
    context = {
        'form': form,
        'edit_choice': True,
        'choice': choice,
    }
    return render(request, 'polls/add_choice.html', context)

@login_required
def choice_delete(request, choice_id):
    choice = get_object_or_404(Choice, pk=choice_id)
    poll = get_object_or_404(Poll, pk=choice.poll.id)
    choice.delete()
    messages.success(
        request, "Choice Deleted successfully.", extra_tags='alert alert-success alert-dismissible fade show')
    return redirect('polls:editPoll', poll.id)
    
